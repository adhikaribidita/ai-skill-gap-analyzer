BLOB_CURSOR_HTML = """
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
</head>
<body>
  <script>
    // Configuration matching the oceanic/purple theme
    const blobType = 'circle';
    const fillColor = '#8b5cf6'; 
    const trailCount = 3;
    const sizes = [50, 100, 60];
    const innerSizes = [15, 25, 15];
    const innerColor = 'rgba(255,255,255,0.9)';
    const opacities = [0.8, 0.6, 0.5];
    const shadowColor = 'rgba(139, 92, 246, 0.6)';
    const shadowBlur = 10;
    const shadowOffsetX = 0;
    const shadowOffsetY = 0;
    const filterId = 'blob-cursor-filter';
    const filterStdDeviation = 25;
    const filterColorMatrixValues = '1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 35 -10';
    const useFilter = true;
    const fastDuration = 0.15;
    const slowDuration = 0.6;
    const fastEase = 'power3.out';
    const slowEase = 'power1.out';
    const zIndex = 99999; 

    const parentDoc = window.parent.document;
    
    // Create container
    const container = parentDoc.createElement('div');
    container.id = "blob-cursor-container";
    Object.assign(container.style, {
      position: 'fixed',
      top: '0', left: '0',
      width: '100vw', height: '100vh',
      pointerEvents: 'none', // Critical: pass clicks through to Streamlit
      zIndex: zIndex,
      overflow: 'hidden'
    });

    // Create SVG filter
    if (useFilter) {
      const svg = parentDoc.createElementNS('http://www.w3.org/2000/svg', 'svg');
      Object.assign(svg.style, { position: 'absolute', width: '0', height: '0' });
      svg.innerHTML = `
        <filter id="${filterId}">
          <feGaussianBlur in="SourceGraphic" result="blur" stdDeviation="${filterStdDeviation}" />
          <feColorMatrix in="blur" values="${filterColorMatrixValues}" />
        </filter>
      `;
      container.appendChild(svg);
    }

    // Create main wrapper
    const mainWrap = parentDoc.createElement('div');
    Object.assign(mainWrap.style, {
      position: 'absolute',
      width: '100%', height: '100%',
      filter: useFilter ? `url(#${filterId})` : 'none'
    });
    container.appendChild(mainWrap);

    // Create blobs
    const blobs = [];
    for (let i = 0; i < trailCount; i++) {
      const blob = parentDoc.createElement('div');
      Object.assign(blob.style, {
        position: 'absolute',
        width: sizes[i] + 'px',
        height: sizes[i] + 'px',
        borderRadius: blobType === 'circle' ? '50%' : '0%',
        backgroundColor: fillColor,
        opacity: opacities[i],
        boxShadow: `${shadowOffsetX}px ${shadowOffsetY}px ${shadowBlur}px 0 ${shadowColor}`,
        willChange: 'transform',
        transform: 'translate(-50%, -50%)',
        left: '0px', top: '0px'
      });

      const inner = parentDoc.createElement('div');
      Object.assign(inner.style, {
        position: 'absolute',
        width: innerSizes[i] + 'px',
        height: innerSizes[i] + 'px',
        top: ((sizes[i] - innerSizes[i]) / 2) + 'px',
        left: ((sizes[i] - innerSizes[i]) / 2) + 'px',
        backgroundColor: innerColor,
        borderRadius: blobType === 'circle' ? '50%' : '0%'
      });

      blob.appendChild(inner);
      mainWrap.appendChild(blob);
      blobs.push(blob);
    }

    parentDoc.body.appendChild(container);

    // Center initially
    gsap.set(blobs, { x: window.parent.innerWidth / 2, y: window.parent.innerHeight / 2 });

    // Handle mouse move
    const handleMove = (e) => {
      const x = e.clientX || (e.touches && e.touches[0].clientX);
      const y = e.clientY || (e.touches && e.touches[0].clientY);
      if (x === undefined || y === undefined) return;

      blobs.forEach((el, i) => {
        const isLead = i === 0;
        gsap.to(el, {
          x: x,
          y: y,
          duration: isLead ? fastDuration : slowDuration,
          ease: isLead ? fastEase : slowEase
        });
      });
    };

    parentDoc.addEventListener('mousemove', handleMove);
    parentDoc.addEventListener('touchmove', handleMove);

    // Cleanup on unmount (when iframe is destroyed on page change)
    window.addEventListener('unload', () => {
      parentDoc.removeEventListener('mousemove', handleMove);
      parentDoc.removeEventListener('touchmove', handleMove);
      if (container.parentNode) container.parentNode.removeChild(container);
    });
  </script>
</body>
</html>
"""
