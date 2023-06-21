# Data Science Introduction

This repository serves as an introduction to the field of data science, covering fundamental concepts, processes, and tools. It's a great starting point for anyone interested in the field, whether you're a novice data enthusiast, a budding data scientist, or an experienced professional looking to refresh your knowledge.
<br>
<br>

### Data science
Coding, statistics, domain expertise ----> Data science

Coding:
- gather, prepare
- stats (R, Python)
- databases (SQL)
- command line (bash)
- search engines (regex)

Math:
- probability, algebra, regression

Domain expertise:
- expertise in the field
- goal, methods and constraints

![](https://i.imgur.com/KT8f09M.png)

- ML (coding and math without domain expertise); black box models
- Research (math and domain without coding); data is structured; effort is in method and in interpretation
- Danger zone (coding and domain without math)

DS pathway:
1. planning:
    - define goals
    - organize resources
    - coordinate people
    - schedule project
2. Data preparation:
    - gather data
    - clean data
    - explore data
    - refine data
3. Modeling:
    - create model
    - validate model
    - evaluate model
    - refine model
4. Follow-up:
    - present model
    - deploy model
    - monitor model
    - archive assets
isn't just technical context is important

#### Roles in data science
- Data engineer: focus on back end hardware and software, manage data pipelines, databases, etc.
- Big data engineer: focus on computer science and math, ML and data products
- Research scientist: focus on specific domain, statistics and math
- Analyst: focus on business, web analytics, SQL; structured data
- Business intelligence: focus on business relevant data
- Entrepreneur: need data & business, creative throughout
- Full-stack unicorn

DS is diverse, different roles, different skills, different goals

#### Big data
![](https://i.imgur.com/Mxawmc3.png)

Big data science:
- volume, velocity, variety in data
- coding, stat, domain expertise

#### Data science vs statistics
- most ds are not statisticians
- ml and big data are not shared with statistics
- data science is not a subset of statistics
- both analyze data, but different goals, niches

============================================================
<br>
Data gathering:
- existing data: in house, public, commercial
- APIs: application programming interface
- scraping: web scraping, screen scraping, data scraping
- make your own data: surveys, experiments

Math:
- calculus
- linear algebra
- probability
- Bayes theorem
- Big O notation

Statistics: (find patterns in data)
- exploratory graphics
- exploratory statistics
- descriptive stats

ML: (categorize & predict)
- Dimensionality reduction
- Clustering
- K-Means
- Anomaly detection
- Categories: Logistic regression, kNN, Naive Bayes, SVM, Decision trees, Neural networks
- Prediction: Linear regression, Poisson regression, Ensemble models
<br>
<br>
### Existing Data sourcing
1. - in house:
     - can be fast and easy
     - Format?
     - Documentation?
     - Quality?
     - Restrictions?
<br>
<br>
    - public:
          - data.gov; open-data.europa.eu
          - unicef.org/statistics; who.int/gho
          - pewinternet.org/datasets
          - developer.nytimes.com
          - google.com/publicdata
          - aws.amazon.com/datasets
      - PRO: Valuable, range of topics, well formatted and documented
      - CON: Bias sampling, meaning not clear, Need to share ana, issues with privacy & confidentiality
  <br>
  <br>
    - commercial - Third party data vendors
        - DaaS: Data as a service
        - Many topics, many formats
        - Nielsen (media), Experian, Acxiom (marketing data), Dunnhumby
        - PRO: Well formatted, well documented, high quality
        - CON: Expensive, restrictions on use, privacy & confidentiality

2. APIs
    - REST: Representational state transfer
       - access to data via HTTP
       - JSON
- Social media APIs
    - Twitter, Facebook, Instagram, LinkedIn, etc.
- Visual APIs
    - Google Maps, Flickr, YouTube, etc.
    - Accu Weather, Open Weather Map
- R, Python, Bash

3. Scraping
    - Web scraping
        - HTML text, HTML tables, pdf-s, media
    - APPS
        - import.io
        - ScraperWiki
        - Tabula
        - Google Sheets
        - Excel
        - R, Python, Bash, php
    - PRO: Fast, easy, cheap
    - CON: Legal issues, technical issues, ethical issues


### Make your own data
1. Interviews
    - new topic, audience, you need find ways to improve
    - Structured interviews
        - same questions, same order
        - PRO: easy to analyze
        - CON: not flexible
    - Unstructured interviews
        - PRO: flexible
        - CON: hard to analyze
    - Time consuming, training, analysis
    - Best for new topics & audiences

2. Card sorting
   - mental model (how people think about a topic intuitively)
   - write topics on cards, ask people to sort them
   - Calculate dissimilarity index
   - Generative card sorting
     - respondents create their own categories
     - used to create website
   - Evaluative card sorting
     - respondents sort cards into pre-defined categories
     - used to evaluate website
   - Dendrograms (hierarchical clustering)
   - Digital card sorting
     -  Optimal Workshop
     -  UserZoom
     -  UX Suite

3. Lab experiments
 - cause and effect
 - Researcher controls the environment
   - Focus research
   - Hypothesis driven
   - Random assignment
   - Confounds & artifacts
 - Eye tracking in WEB design
 - Expensive, time consuming, labor intensive, requires expertise and training

4. A/B testing
 - compare two versions of a website
 - Randomly assign users to one of two versions
 - Measure performance, response rate (clicks, purchases, etc.)
 - Implement the best version
 - software: Optimizely, VWO
 - PRO: Easy, fast, cheap
 - CON: Limited to website, limited to two versions, limited to performance

5. Surveys
   - Questionnaires
   - closed-ended questions
   - open-ended questions
   - in person, phone, mail, email, web
   - survey monkey, google forms, typeform, Qualtrics
   - PRO: Easy, fast, cheap
   - CON: Limited to questions, limited to responses, watch out for bias
   - Beware the push poll (biased questions)
<br>
<br>
### Coding (manipulate data)

data tools != data science

- spreadsheets, Tableau (visualization), Web data
- R, Python, SQL
- C, C++, Java, Bash, Regex

1. Applications
   - Excel, Google Sheets
     - they are everywhere, clients use them
     - data transfer (csv)
     - data browsing, sorting, rearranging, find and replace
     - formatting, transposing, tracking changes, pivot tables, arranging output
     - Tidy data:
        - for transferring data
        - columns == variables
        - rows ==  case
        - One sheet per file
        - one level per file
  <br>
  <br>

   - Tableau and Tableau Public
    - Visualization
    - drag and drop
   <br>
   <br>

   - SPSS
     - Statistical package for the social sciences
     - ibm.com/spss
     - automate data analysis with syntax
 <br>
 <br>

   - JASP
     - open source
     - jasp-stats.org
     - alternative to SPSS
     - you can share your analysis with OSF.io
  <br>
  <br>

   - Other statistical software
     - SAS
     - JMP (visualization)
     - Stata
     - Minitab
     - Matlab
     - Mathematica
     - Wolfram Alpha
     - Data mining:
       - rapidminer
       - KNIME
       - Orange
     - BigMl
     - Sofa Statistics
     - Past 3
     - StatCrunch
     - XLSTAT
 <br>
 <br>
  - HTML
      - uses tags to mark up text
      - defines structure of web pages
 <br>
 <br>
  - XML
    - semi-structured data
    - markup language, alow commenting and metadata
    - Tags define structure of data
    - Tags can be user defined
    - WEB data, MS office, ITunes, Data files
    - Tags using angle brackets
      <br>
      <#genere></#genere>
      <#composer></#composer>
      <br>
    - convertible XML ---> CSV; HTML ---> XML; CSV ---> XML
  <br>
  <br>
    - JSON
     - JavaScript Object Notation
     - semi-structured data
     - design for data interchange
     - corresponds with data structures
     - shorter than XML
     - taking over XML
     - east to convert

2. Coding languages
  - R
     - free & open source
     - vector operations
     - 7k+ packages (CRAN cran.rstudio.com; Crantastic crantastic.org ---> show popular packages & updates)
     - IDS: RStudio, Jupyter
     - idiosyncratic syntax
  <br>
  <br>
  - Python
     - Only general purpose language for data science
     - NumPy, SciPy, Pandas, Matplotlib, Seaborn, Scikit-learn
  <br>
  <br>
  - SQL
    - Structured Query Language
    - Relational databases, STRUCTURED data
    - RDBMS: Relational database management system (MySQL, PostgreSQL, SQLite, Oracle, Microsoft SQL Server)
    - SELECT, FROM, WHERE, GROUP BY, ORDER BY, JOIN
  <br>
  <br>
   - C, C++, Java:
     - low level, high performance
     - fast & stable
     - java is based on C/C++
       - WORA (write once, run anywhere)
     - data's backed
  <br>
  <br>
   - Bash
     - CLI
     - method of interacting with computer at CLI level
     - scripting
     - build in utilities:
       - cat
       - awk
       - grep
       - sed
       - head & tail
       - sort
       - wc
       - printf
     - install packages
       - jq
       - json2csv
       - Rio
       - BigMler (access to BigML API)
  <br>
  <br>
   - Regex
    - from of pattern matching
    - specific & general
    - Elements:
      - Literal characters
      - Metacharacters
      - Escaped sequences
      - Search expression
      - Target string
          - ^: start of string (Ex: ^a); start with a
          - $: end of string (Ex: a$); end with a
          - .: any character (Ex: a.c); a + any character + c
     - regex.alf.nu
     - use for the find right data
<br>
<br>
### Mathematical foundations

- Linear algebra
- Systems of linear equations
- Calculus
- Big O notation
- Probability
- Bayes' theorem
<br>
<br>
### Statistics in data science

- Methods
  - Descriptive statistics
  - Inferential statistics
  - Hypothesis testing
  - Estimation
<br>
<br>


Link to original content:
1. [Data Science Introduction](https://www.youtube.com/watch?v=ua-CiDNNj30&list=PLkNZMXPAMnwPWawqMHs5Y2Q5B3Sh5Iwbo&index=2)
2. [Data Structures](https://www.youtube.com/watch?v=zg9ih6SVACc&list=PLkNZMXPAMnwPWawqMHs5Y2Q5B3Sh5Iwbo&index=3&t=115s)











