def analyze_gap(user_skills, required_skills):
    """
    Compares user skills against required skills and returns the gap.
    """
    user_skills_set = set(user_skills)
    required_skills_set = set(required_skills)
    
    missing_skills = list(required_skills_set - user_skills_set)
    matched_skills = list(required_skills_set.intersection(user_skills_set))
    
    match_percentage = 0
    if len(required_skills) > 0:
        match_percentage = (len(matched_skills) / len(required_skills)) * 100
        
    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(match_percentage, 2)
    }

# Advanced learning resource mapping for a highly detailed student roadmap
RESOURCE_MAP = {
    "python": {
        "time": "4-6 Weeks",
        "concepts": "Variables, Data Structures, OOP, API Requests, Data Processing.",
        "course": "Python for Everybody Specialization", 
        "url": "https://www.coursera.org/specializations/python",
        "project_title": "Automated E-Commerce Price Tracker",
        "project_abstract": "**Problem Statement:** Manually checking product prices across multiple websites is tedious and inefficient. Consumers need a way to track price drops automatically to save money.\n\n**Abstract:** Build a robust Python script using BeautifulSoup and Requests to scrape product data. Implement SQLite to store historical prices and use the smtplib library to send automated email alerts when prices drop below a threshold. This demonstrates web scraping, database management, and automation."
    },
    "sql": {
        "time": "3-5 Weeks",
        "concepts": "Joins, Aggregations, Window Functions, Subqueries, Indexing Optimization.",
        "course": "SQL for Data Science", 
        "url": "https://www.coursera.org/learn/sql-for-data-science",
        "project_title": "E-Commerce Analytics Data Warehouse",
        "project_abstract": "**Problem Statement:** Business stakeholders lack visibility into sales trends and customer purchasing behavior, preventing data-driven decision making.\n\n**Abstract:** Design a complex relational database schema (Users, Orders, Products, Reviews). Write complex analytical queries using Window Functions to find 'Top 5 spending users per month' and 'Month-over-month sales growth'. Optimize the queries using proper Indexing."
    },
    "machine learning": {
        "time": "8-12 Weeks",
        "concepts": "Linear Regression, Random Forests, Scikit-Learn, Model Evaluation, Hyperparameter Tuning.",
        "course": "Machine Learning Specialization", 
        "url": "https://www.coursera.org/specializations/machine-learning-introduction",
        "project_title": "Real-Estate Price Predictor API",
        "project_abstract": "**Problem Statement:** Homebuyers and sellers often struggle to determine fair market value for properties based on varying features like location, square footage, and age.\n\n**Abstract:** Train a predictive model using Scikit-Learn on a real-world housing dataset. Perform feature engineering (handling missing values, one-hot encoding). Expose the trained model via a FastAPI endpoint where users can input house features and receive an instant price prediction."
    },
    "statistics": {
        "time": "4-6 Weeks",
        "concepts": "Probability Distributions, Hypothesis Testing, A/B Testing, Bayesian Inference.",
        "course": "Statistics with Python Specialization",
        "url": "https://www.coursera.org/specializations/statistics-with-python",
        "project_title": "E-Commerce A/B Test Evaluator",
        "project_abstract": "**Problem Statement:** Product teams often launch new UI designs but struggle to statistically prove whether the new design actually increased the checkout conversion rate without relying on gut feeling.\n\n**Abstract:** Analyze a massive dataset of user interactions. Perform rigorous A/B hypothesis testing (T-tests, Chi-Square) to determine if a new feature drove a statistically significant uplift. Present the findings in a comprehensive Jupyter Notebook."
    },
    "data visualization": {
        "time": "3-4 Weeks",
        "concepts": "Matplotlib, Seaborn, Tableau, Dashboards, Storytelling with Data.",
        "course": "Data Visualization with Python",
        "url": "https://www.coursera.org/learn/python-for-data-visualization",
        "project_title": "Global Climate Change Dashboard",
        "project_abstract": "**Problem Statement:** Raw climate data (temperatures, CO2 levels) is difficult for the general public and policymakers to digest, hindering urgent climate action.\n\n**Abstract:** Build an interactive dashboard using Plotly Dash or Streamlit that visualizes 50 years of global temperature shifts. Implement interactive sliders for time-series forecasting and choropleth maps to show regional impacts."
    },
    "pandas": {
        "time": "2-3 Weeks",
        "concepts": "DataFrames, Series, Merging, Groupby, Handling Missing Data.",
        "course": "Data Analysis with Pandas and Python",
        "url": "https://www.udemy.com/course/data-analysis-with-pandas/",
        "project_title": "Financial Portfolio Analyzer",
        "project_abstract": "**Problem Statement:** Retail investors often have scattered financial data across multiple brokerages and CSV formats, making it impossible to see their true net worth and asset allocation.\n\n**Abstract:** Write a Pandas pipeline that ingests messy CSV exports from Robinhood, Coinbase, and Vanguard. Clean the data, normalize the currencies, and group by asset class to generate a unified, clean portfolio summary."
    },
    "numpy": {
        "time": "1-2 Weeks",
        "concepts": "N-dimensional Arrays, Broadcasting, Vectorization, Linear Algebra.",
        "course": "Deep Learning Prerequisites: The Numpy Stack",
        "url": "https://www.udemy.com/course/deep-learning-prerequisites-the-numpy-stack-in-python/",
        "project_title": "High-Performance Image Filter Engine",
        "project_abstract": "**Problem Statement:** Applying image filters pixel-by-pixel using standard loops in Python is unacceptably slow for high-resolution images.\n\n**Abstract:** Read image data as multi-dimensional NumPy arrays. Apply complex transformations (grayscale, edge detection via Sobel operators, blurring) using pure NumPy vectorization and matrix multiplication to achieve 100x performance gains over native loops."
    },
    "deep learning": {
        "time": "10-14 Weeks",
        "concepts": "Neural Networks, CNNs, RNNs, PyTorch, TensorFlow, Backpropagation.",
        "course": "Deep Learning Specialization",
        "url": "https://www.coursera.org/specializations/deep-learning",
        "project_title": "Medical Image Disease Classifier",
        "project_abstract": "**Problem Statement:** Medical professionals need fast, preliminary screening tools to identify potential diseases from medical imaging before detailed human analysis.\n\n**Abstract:** Use PyTorch to build a Convolutional Neural Network (CNN) that analyzes X-ray images to detect pneumonia. Utilize transfer learning (ResNet50) to achieve high accuracy with limited data. Output a heatmap showing which parts of the X-ray influenced the model's decision."
    },
    "nlp": {
        "time": "6-8 Weeks",
        "concepts": "Tokenization, Word Embeddings, Transformers, Sentiment Analysis, BERT.",
        "course": "Natural Language Processing Specialization",
        "url": "https://www.coursera.org/specializations/natural-language-processing",
        "project_title": "Automated Customer Support Router",
        "project_abstract": "**Problem Statement:** Large companies receive thousands of support tickets daily. Manually reading and routing these tickets to the correct department causes massive delays in resolution times.\n\n**Abstract:** Fine-tune a pre-trained language model (like BERT or RoBERTa) on a dataset of customer service transcripts. The model should classify the intent of an incoming email and automatically route it to Billing, Tech Support, or Sales."
    },
    "tensorflow": {
        "time": "4-6 Weeks",
        "concepts": "Tensors, Keras API, Model Deployment, TF Record, Custom Training Loops.",
        "course": "TensorFlow Developer Professional Certificate",
        "url": "https://www.coursera.org/professional-certificates/tensorflow-in-practice",
        "project_title": "Real-time Defect Detection for Manufacturing",
        "project_abstract": "**Problem Statement:** Assembly lines rely on manual visual inspection to find defective products, which is slow and prone to human fatigue and error.\n\n**Abstract:** Build and train an Object Detection model using the TensorFlow Object Detection API to identify scratches and dents on manufactured parts. Export the model and deploy it via TensorFlow Serving for real-time inference on a factory floor."
    },
    "pytorch": {
        "time": "4-6 Weeks",
        "concepts": "Tensors, Autograd, nn.Module, DataLoaders, GPU Acceleration.",
        "course": "Deep Neural Networks with PyTorch",
        "url": "https://www.coursera.org/learn/deep-neural-networks-with-pytorch",
        "project_title": "Generative Art using GANs",
        "project_abstract": "**Problem Statement:** Digital artists and game developers need inspiration and rapid prototyping tools for creating unique character textures and landscapes.\n\n**Abstract:** Implement a Generative Adversarial Network (GAN) from scratch in PyTorch. Train it on a dataset of abstract paintings or game assets to generate entirely new, high-resolution artificial artwork."
    },
    "computer vision": {
        "time": "6-8 Weeks",
        "concepts": "Image Processing, OpenCV, Object Detection, Segmentation, YOLO.",
        "course": "First Principles of Computer Vision",
        "url": "https://www.coursera.org/specializations/firstprinciplesofcomputervision",
        "project_title": "Automated Traffic Monitoring System",
        "project_abstract": "**Problem Statement:** City planners need accurate data on traffic volume and vehicle types at intersections, but manually counting cars on video feeds is impossible.\n\n**Abstract:** Use OpenCV and a pre-trained YOLOv8 model to process dashboard camera or CCTV video feeds. Build a tracking algorithm that draws bounding boxes, counts unique vehicles crossing a line, and classifies them as cars, trucks, or motorcycles."
    },
    "llms": {
        "time": "4-6 Weeks",
        "concepts": "Prompt Engineering, RAG, LangChain, Vector Databases, Fine-Tuning.",
        "course": "Generative AI with Large Language Models",
        "url": "https://www.coursera.org/learn/generative-ai-with-llms",
        "project_title": "Enterprise RAG Document Assistant",
        "project_abstract": "**Problem Statement:** Employees spend hours searching through massive internal company wikis and HR PDFs just to find simple policy answers.\n\n**Abstract:** Build a Retrieval-Augmented Generation (RAG) pipeline using LangChain, OpenAI, and a Vector Database (Pinecone or Chroma). Ingest 50+ pages of complex PDF documents so users can ask natural language questions and receive cited, highly accurate answers."
    },
    "java": {
        "time": "6-8 Weeks",
        "concepts": "OOP, Interfaces, Generics, Multithreading, JVM, Spring Boot.",
        "course": "Java Programming and Software Engineering Fundamentals",
        "url": "https://www.coursera.org/specializations/java-programming",
        "project_title": "High-Concurrency Banking System",
        "project_abstract": "**Problem Statement:** Financial applications must handle thousands of simultaneous transactions without race conditions or data corruption.\n\n**Abstract:** Build a core banking backend using Java Spring Boot. Implement multi-threading to handle concurrent deposits and withdrawals securely. Use optimistic locking in a PostgreSQL database to absolutely guarantee data integrity under high load."
    },
    "c++": {
        "time": "8-10 Weeks",
        "concepts": "Pointers, Memory Management, STL, RAII, Object-Oriented Design.",
        "course": "C++ for C Programmers",
        "url": "https://www.coursera.org/learn/c-plus-plus-a",
        "project_title": "Low-Latency Trading Engine Simulator",
        "project_abstract": "**Problem Statement:** Algorithmic trading firms require extreme performance where microseconds matter, making Python or Java too slow due to garbage collection.\n\n**Abstract:** Develop an order matching engine in modern C++. Implement custom memory pools to avoid the overhead of dynamic allocation (new/delete). Use advanced STL data structures to match buy and sell orders with sub-millisecond latency."
    },
    "data structures": {
        "time": "4-6 Weeks",
        "concepts": "Arrays, Linked Lists, Hash Tables, Trees, Graphs, Heaps.",
        "course": "Data Structures and Algorithms Specialization",
        "url": "https://www.coursera.org/specializations/data-structures-algorithms",
        "project_title": "Custom In-Memory Key-Value Store",
        "project_abstract": "**Problem Statement:** Relying solely on out-of-the-box databases obscures the fundamental mechanisms of fast data retrieval, causing developers to write incredibly inefficient queries.\n\n**Abstract:** Build a Redis clone from scratch. Implement your own Hash Map for O(1) lookups, a Min-Heap for setting key expirations/TTL, and an LRU (Least Recently Used) cache eviction policy using a Doubly Linked List."
    },
    "algorithms": {
        "time": "6-8 Weeks",
        "concepts": "Sorting, Searching, Dynamic Programming, Greedy Algorithms, Graph Traversal.",
        "course": "Algorithms, Part I",
        "url": "https://www.coursera.org/learn/algorithms-part1",
        "project_title": "Optimal Delivery Routing Engine",
        "project_abstract": "**Problem Statement:** Delivery drivers waste fuel and time taking suboptimal routes when delivering packages to dozens of addresses.\n\n**Abstract:** Implement Graph algorithms to solve a bounded version of the Traveling Salesperson Problem. Use Dijkstra's and A* search algorithms to calculate the absolute shortest path between 20 geographic coordinates, rendering the result on a map API."
    },
    "system design": {
        "time": "6-10 Weeks",
        "concepts": "Load Balancing, Caching, Microservices, Database Sharding, CAP Theorem.",
        "course": "Grokking the System Design Interview", 
        "url": "https://www.educative.io/courses/grokking-the-system-design-interview",
        "project_title": "Distributed URL Shortener Architecture",
        "project_abstract": "**Problem Statement:** Long URLs break in emails and are hard to share. A service is needed that can reliably redirect billions of short aliases to their original long URLs under high load.\n\n**Abstract:** Write a comprehensive technical design document for a bit.ly clone. Include diagrams detailing the API Gateway, Load Balancers, Redis caching layer for fast redirects, and a sharded database architecture to handle billions of URLs with high availability."
    },
    "git": {
        "time": "1-2 Weeks",
        "concepts": "Branching, Merging, Rebasing, Conflict Resolution, CI/CD Triggers.",
        "course": "Version Control with Git",
        "url": "https://www.coursera.org/learn/version-control-with-git",
        "project_title": "Open Source Collaboration Simulation",
        "project_abstract": "**Problem Statement:** Junior developers often panic when they encounter a merge conflict or accidentally commit secrets, disrupting the entire team's workflow.\n\n**Abstract:** Create a multi-branch repository utilizing Git flow. Intentionally create complex merge conflicts and resolve them using interactive rebase (`git rebase -i`). Implement a GitHub Action (CI/CD) that runs a linter every time a Pull Request is opened."
    },
    "aws": {
        "time": "6-8 Weeks",
        "concepts": "EC2, S3, IAM, Lambda, VPC, CloudFront, Serverless Architectures.",
        "course": "AWS Certified Cloud Practitioner", 
        "url": "https://aws.amazon.com/certification/certified-cloud-practitioner/",
        "project_title": "Serverless Image Processing Pipeline",
        "project_abstract": "**Problem Statement:** Web applications need a cost-effective, infinitely scalable way to handle user-uploaded media without provisioning permanent server infrastructure.\n\n**Abstract:** Set up an S3 bucket where users upload images. Configure an AWS Lambda function to trigger automatically on upload, resize the image, and save the thumbnail to a different bucket. Secure the buckets using IAM policies and serve the thumbnails globally via CloudFront CDN."
    },
    "azure": {
        "time": "6-8 Weeks",
        "concepts": "Virtual Machines, Azure Blob Storage, Azure Functions, Entra ID, ARM Templates.",
        "course": "Microsoft Azure Fundamentals AZ-900",
        "url": "https://docs.microsoft.com/en-us/learn/certifications/azure-fundamentals/",
        "project_title": "Azure Event-Driven Telemetry Processor",
        "project_abstract": "**Problem Statement:** IoT devices generate millions of data points per minute that need to be ingested, processed, and stored without crashing the receiving server.\n\n**Abstract:** Use Azure IoT Hub to ingest simulated sensor data. Route the data using Azure Event Grid to an Azure Function, which processes and cleans the data before depositing it into Azure Cosmos DB for downstream analytics."
    },
    "gcp": {
        "time": "6-8 Weeks",
        "concepts": "Compute Engine, Cloud Storage, BigQuery, Cloud Run, Pub/Sub.",
        "course": "Google Cloud Computing Foundations",
        "url": "https://www.coursera.org/specializations/google-cloud-computing-foundations",
        "project_title": "Serverless Big Data Analytics Pipeline",
        "project_abstract": "**Problem Statement:** Analyzing gigabytes of log data using traditional SQL servers takes hours, delaying critical business intelligence reports.\n\n**Abstract:** Upload massive CSV datasets to Google Cloud Storage. Use Cloud Pub/Sub and Dataflow to stream the data directly into BigQuery. Write lightning-fast analytics queries in BigQuery to process millions of rows in seconds."
    },
    "docker": {
        "time": "2-3 Weeks",
        "concepts": "Images, Containers, Dockerfile Optimization, Docker Compose, Volumes.",
        "course": "Docker Mastery: with Kubernetes +Swarm", 
        "url": "https://www.udemy.com/course/docker-mastery/",
        "project_title": "Microservices Containerization",
        "project_abstract": "**Problem Statement:** The 'it works on my machine' syndrome causes deployment failures and inconsistencies between development and production environments.\n\n**Abstract:** Take an existing full-stack application (e.g. a React frontend, Node.js API, and Postgres database) and write Dockerfiles for each. Use Docker Compose to network them together so the entire stack can be spun up on any machine with a single 'docker-compose up' command."
    },
    "kubernetes": {
        "time": "6-8 Weeks",
        "concepts": "Pods, Deployments, Services, Ingress, ConfigMaps, Auto-scaling.",
        "course": "Kubernetes for Developers",
        "url": "https://www.udemy.com/course/kubernetes-for-developers/",
        "project_title": "Highly Available Microservices Cluster",
        "project_abstract": "**Problem Statement:** If a single server hosting a monolithic application crashes, the entire business goes offline. Applications need self-healing capabilities.\n\n**Abstract:** Deploy a 3-tier microservice architecture to a local Minikube or cloud Kubernetes cluster. Configure Horizontal Pod Autoscalers to automatically add instances during high CPU load. Implement rolling updates to ensure zero-downtime deployments."
    },
    "linux": {
        "time": "3-4 Weeks",
        "concepts": "Bash Scripting, File Permissions, Process Management, Cron Jobs, SSH.",
        "course": "Linux Mastery: Master the Linux Command Line",
        "url": "https://www.udemy.com/course/linux-mastery/",
        "project_title": "Automated Server Hardening and Backup Script",
        "project_abstract": "**Problem Statement:** Newly provisioned Linux servers have default configurations that are vulnerable to automated attacks and data loss.\n\n**Abstract:** Write a comprehensive Bash script that automatically disables root SSH login, configures UFW (Uncomplicated Firewall) to only allow ports 80/443, and sets up a Cron job that securely uses Rsync to backup the `/var/www` directory to a remote server nightly."
    },
    "networking": {
        "time": "4-6 Weeks",
        "concepts": "TCP/IP, DNS, Subnetting, OSI Model, HTTP/HTTPS, VPNs.",
        "course": "Computer Networking",
        "url": "https://www.coursera.org/learn/computer-networking",
        "project_title": "Custom TCP Chat Server",
        "project_abstract": "**Problem Statement:** Without understanding the underlying TCP layer, developers struggle to debug slow web applications or network timeouts.\n\n**Abstract:** Build a multi-client chat server using raw TCP sockets in Python or C. Handle packet fragmentation manually. Implement a custom binary protocol header to ensure that messages arrive intact, demonstrating a deep understanding of the Transport Layer."
    },
    "terraform": {
        "time": "3-4 Weeks",
        "concepts": "Providers, State Management, Modules, Variables, Provisioners.",
        "course": "HashiCorp Certified: Terraform Associate",
        "url": "https://www.udemy.com/course/terraform-beginner-to-advanced/",
        "project_title": "Infrastructure as Code (IaC) Pipeline",
        "project_abstract": "**Problem Statement:** Clicking through AWS/GCP consoles to provision infrastructure is error-prone, unrepeatable, and impossible to version control.\n\n**Abstract:** Write declarative HCL (HashiCorp Configuration Language) modules to deploy a VPC, private subnets, security groups, and an EC2 instance. Store the Terraform State securely in a remote S3 bucket with DynamoDB state locking to allow team collaboration."
    },
    "react": {
        "time": "4-6 Weeks",
        "concepts": "Components, State Management (Redux/Zustand), Hooks, React Router, Next.js.",
        "course": "React - The Complete Guide", 
        "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/",
        "project_title": "Dynamic Movie Discovery Web App",
        "project_abstract": "**Problem Statement:** Users need a responsive, highly interactive web application to browse, search, and save their favorite trending movies from a massive database.\n\n**Abstract:** Build a responsive frontend using React and TailwindCSS. Integrate with the TMDB REST API to fetch trending movies. Implement complex state management for a 'Favorites' watchlist, and use React Router for seamless navigation between movie detail pages."
    },
    "javascript": {
        "time": "4-6 Weeks",
        "concepts": "ES6+, Closures, Promises/Async Await, Event Loop, DOM Manipulation.",
        "course": "The Complete JavaScript Course",
        "url": "https://www.udemy.com/course/the-complete-javascript-course/",
        "project_title": "Vanilla JS Single Page Application (SPA)",
        "project_abstract": "**Problem Statement:** Relying exclusively on frameworks like React obscures how the browser DOM actually works, making it hard to debug profound performance issues.\n\n**Abstract:** Build a fully functional Single Page Application (SPA) utilizing the History API for routing without page reloads. Fetch and display remote API data using Promises, and handle state changes purely through Native DOM manipulation without any external libraries."
    },
    "html": {
        "time": "1-2 Weeks",
        "concepts": "Semantic Tags, Accessibility (a11y), Forms, SEO Basics.",
        "course": "HTML, CSS, and Javascript for Web Developers",
        "url": "https://www.coursera.org/learn/html-css-javascript-for-web-developers",
        "project_title": "Accessible E-Commerce Product Page",
        "project_abstract": "**Problem Statement:** Many modern websites are completely unusable for visually impaired users relying on screen readers because developers ignore semantic HTML.\n\n**Abstract:** Build a comprehensive product page using strict semantic HTML5 (`<article>`, `<nav>`, `<aside>`). Ensure a perfect 100/100 Lighthouse Accessibility score by properly implementing ARIA labels, `alt` tags, and a keyboard-navigable checkout form."
    },
    "css": {
        "time": "2-4 Weeks",
        "concepts": "Flexbox, CSS Grid, Responsive Design, Animations, SASS.",
        "course": "Advanced CSS and Sass",
        "url": "https://www.udemy.com/course/advanced-css-and-sass/",
        "project_title": "Responsive Glassmorphism Dashboard UI",
        "project_abstract": "**Problem Statement:** Applications that look great on a 4K monitor often completely break on mobile devices, leading to terrible user retention.\n\n**Abstract:** Develop a complex analytics dashboard layout without using any CSS frameworks. Utilize CSS Grid for the macro-layout and Flexbox for micro-alignments. Implement media queries to seamlessly reflow the dashboard into a mobile-friendly view, utilizing modern aesthetics like glassmorphism and keyframe animations."
    },
    "node.js": {
        "time": "4-6 Weeks",
        "concepts": "Event-Driven Architecture, Express.js, RESTful APIs, JWT Authentication, WebSockets.",
        "course": "NodeJS - The Complete Guide",
        "url": "https://www.udemy.com/course/nodejs-the-complete-guide/",
        "project_title": "Real-Time Collaborative Task Manager",
        "project_abstract": "**Problem Statement:** Standard REST APIs require the client to constantly refresh the page to see updates made by other users, creating a disjointed collaborative experience.\n\n**Abstract:** Build a backend API using Node.js and Express. Implement stateless JWT authentication for secure login. Utilize Socket.io (WebSockets) to push real-time updates to all connected clients whenever a task is created, moved, or deleted, simulating a live Trello board."
    },
    "agile": {
        "time": "1-2 Weeks",
        "concepts": "Sprints, User Stories, Retrospectives, Kanban, Estimation.",
        "course": "Agile Development Specialization",
        "url": "https://www.coursera.org/specializations/agile-development",
        "project_title": "Agile Workflow Implementation Strategy",
        "project_abstract": "**Problem Statement:** Software teams without a structured methodology suffer from scope creep, missed deadlines, and complete developer burnout.\n\n**Abstract:** Adopt the role of a Scrum Master for a hypothetical massive software rewrite. Write a comprehensive set of User Stories with acceptance criteria. Set up a Jira or Trello board, estimate story points using planning poker, and document a mock Sprint Retrospective."
    },
    "scrum": {
        "time": "1-2 Weeks",
        "concepts": "Scrum Master, Product Owner, Daily Standups, Backlog Refinement.",
        "course": "Scrum Master Certification Preparation",
        "url": "https://www.coursera.org/learn/scrum-master-certification",
        "project_title": "Scrum Artifacts and Ceremonies Playbook",
        "project_abstract": "**Problem Statement:** Organizations often claim to 'do Scrum' but fail because they only implement the Daily Standup while ignoring the critical review and refinement phases.\n\n**Abstract:** Draft a professional playbook outlining how to rescue a failing project using strict Scrum. Define the precise responsibilities of the Product Owner, simulate a Backlog Refinement session ordering priorities by business value, and execute a burndown chart analysis."
    },
    "penetration testing": {
        "time": "6-8 Weeks",
        "concepts": "Vulnerability Scanning, Exploitation, Metasploit, Privilege Escalation, Social Engineering.",
        "course": "Penetration Testing, Incident Response and Forensics",
        "url": "https://www.coursera.org/learn/ibm-penetration-testing-incident-response-forensics",
        "project_title": "Corporate Active Directory Compromise Simulation",
        "project_abstract": "**Problem Statement:** Companies are often completely unaware of how easily their internal network can be taken over if a single employee's machine is compromised.\n\n**Abstract:** Set up an isolated lab using virtual machines with a Windows Server Domain Controller and a Kali Linux attacker machine. Execute a full cyber kill-chain: perform initial reconnaissance, exploit a known vulnerability using Metasploit, extract password hashes using Mimikatz, and escalate to Domain Admin privileges. Write a professional remediation report."
    },
    "network security": {
        "time": "4-6 Weeks",
        "concepts": "Firewalls, IDS/IPS, VPNs, Zero Trust, DDoS Mitigation.",
        "course": "Network Security & Database Vulnerabilities",
        "url": "https://www.coursera.org/learn/network-security-database-vulnerabilities",
        "project_title": "Enterprise Cloud DMZ Architecture",
        "project_abstract": "**Problem Statement:** Storing a database on a public-facing web server guarantees a data breach. Networks must be segmented to isolate critical data from public traffic.\n\n**Abstract:** Design and implement a highly secure network topology in AWS or a local virtual environment. Configure a Demilitarized Zone (DMZ) with strict firewall rules, deploy an Intrusion Detection System (Snort or Suricata) to monitor traffic anomalies, and establish a secure VPN tunnel for remote administrative access."
    },
    "wireshark": {
        "time": "2-3 Weeks",
        "concepts": "Packet Sniffing, PCAP Analysis, Protocol Dissection, Network Troubleshooting.",
        "course": "Wireshark for Network Security",
        "url": "https://www.udemy.com/course/wireshark-packet-analysis-and-ethical-hacking-core-skills/",
        "project_title": "Malware Traffic Forensics Investigation",
        "project_abstract": "**Problem Statement:** When a cyber attack happens, incident responders must reconstruct the exact sequence of events by analyzing raw network traffic.\n\n**Abstract:** Obtain a real-world PCAP file of a ransomware infection (e.g., from Malware-Traffic-Analysis.net). Use Wireshark to filter out the noise, identify the exact payload delivery mechanism (like a malicious macro downloading an executable via HTTP), and extract the attacker's Command and Control (C2) IP address."
    },
    "cryptography": {
        "time": "4-6 Weeks",
        "concepts": "Symmetric/Asymmetric Encryption, Hashing, RSA, AES, PKI, Digital Signatures.",
        "course": "Cryptography I by Stanford University",
        "url": "https://www.coursera.org/learn/crypto",
        "project_title": "End-to-End Encrypted Messenger",
        "project_abstract": "**Problem Statement:** Standard messaging apps store chat histories in plaintext on centralized servers, exposing users to surveillance and mass data breaches.\n\n**Abstract:** Build a secure chat application using Python or Node.js. Implement a hybrid cryptography model: use RSA key pairs to establish a secure handshake and exchange a symmetric AES key, then use the AES key to encrypt the actual chat messages. Ensure the server only routes encrypted ciphertexts and never holds the private keys."
    },
    "operating systems": {
        "time": "8-10 Weeks",
        "concepts": "Process Scheduling, Memory Management, Paging, Concurrency, File Systems.",
        "course": "Computer Architectures and Operating Systems",
        "url": "https://www.coursera.org/specializations/computer-architecture-operating-systems",
        "project_title": "Custom Multithreaded Web Server in C",
        "project_abstract": "**Problem Statement:** High-level frameworks abstract away how operating systems actually handle network requests, leading to inefficient code that collapses under high concurrency.\n\n**Abstract:** Build an HTTP web server from scratch in C or Rust using raw POSIX system calls. Implement a thread pool to handle concurrent incoming TCP connections without blocking. Utilize Mutexes and Condition Variables to safely manage shared memory across threads, demonstrating a profound understanding of OS process management."
    },
    "computer architecture": {
        "time": "6-8 Weeks",
        "concepts": "CPU Design, Pipelining, Cache Hierarchy, Instruction Set Architecture (ISA).",
        "course": "Build a Modern Computer from First Principles: From Nand to Tetris",
        "url": "https://www.coursera.org/learn/build-a-computer",
        "project_title": "16-bit Virtual CPU Emulator",
        "project_abstract": "**Problem Statement:** Software engineers who don't understand how CPUs execute binary instructions write code that thrashes the cache and destroys performance.\n\n**Abstract:** Write a software emulator for a simplified 16-bit CPU architecture (like the LC-3 or CHIP-8). Implement the Fetch-Decode-Execute cycle, simulate the Program Counter, ALU, and registers, and write a simple assembly language program that can run perfectly on your emulated hardware."
    },
    "compilers": {
        "time": "8-12 Weeks",
        "concepts": "Lexical Analysis, Parsing, ASTs, Intermediate Representation, Code Generation.",
        "course": "Compilers by Stanford University",
        "url": "https://online.stanford.edu/courses/soe-ycscs1-compilers",
        "project_title": "Custom Programming Language Parser",
        "project_abstract": "**Problem Statement:** Relying on external domain-specific languages (DSLs) is often restrictive. Sometimes, teams need to parse custom logic configurations natively.\n\n**Abstract:** Design a minimalist, domain-specific programming language. Build a Lexer to tokenize the input strings, and write a Recursive Descent Parser to generate an Abstract Syntax Tree (AST). Write a Tree-Walking Interpreter that can evaluate mathematical expressions and logical control flow (if/else statements) written in your newly created language."
    }
}

def generate_roadmap(missing_skills):
    """
    Generates a highly detailed, student-focused roadmap based on missing skills.
    """
    if not missing_skills:
        return ["You have all the required core skills for this role!"]
        
    roadmap = []
    
    for i, skill in enumerate(missing_skills, 1):
        roadmap.append(f"#### Module {i}: Master {skill.title()}")
        
        # Check if we have a specific advanced recommendation
        if skill.lower() in RESOURCE_MAP:
            rec = RESOURCE_MAP[skill.lower()]
            roadmap.append(f"⏳ **Estimated Timeline:** {rec['time']}")
            roadmap.append(f"🧠 **Core Concepts to Master:** {rec['concepts']}")
            roadmap.append(f"Recommended Course: [{rec['course']}]({rec['url']})")
            roadmap.append(f"Capstone Project: **{rec['project_title']}**")
            roadmap.append(f"Project Abstract: {rec['project_abstract']}")
        else:
            roadmap.append("⏳ **Estimated Timeline:** 3-5 Weeks")
            roadmap.append(f"🧠 **Core Concepts to Master:** Fundamentals and advanced patterns of {skill.title()}.")
            roadmap.append(f"Recommended Course: [{skill.title()} Masterclass (YouTube Search)](https://www.youtube.com/results?search_query={skill.replace(' ', '+')}+full+course)")
            roadmap.append(f"Capstone Project: **Real-world {skill.title()} Implementation**")
            roadmap.append(f"Project Abstract: **Problem Statement:** Abstract knowledge of {skill.title()} is insufficient for enterprise environments without practical implementation experience.\n\n**Abstract:** Build a personal portfolio project demonstrating your ability to use {skill.title()} in a real-world scenario. Focus on solving a specific problem, implementing best practices, and deploying the solution to a public repository like GitHub with clear documentation.")
        
    return roadmap
