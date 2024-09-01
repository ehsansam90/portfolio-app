from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

from django.shortcuts import render

from .models import newyorknearby_trends, sandiegonearby_trends, sanfrancisconearby_trends

# Create your views here.
# main/views.py
def home(request):
    return render(request, 'main/home.html')

def resume(request):
    # Hardcoded resume data
    personal_info = {
        'name': 'Ehsan Soltanmohammadi',
        'phone': '+1 803 269 4426',
        'email': ['Ehsans@email.sc.edu', 'Ehsannsam@gmail.com'],
        'linkedin': 'https://linkedin.com/in/ehsansm/'
    }

    experience = [
        {
            'role': 'Data Engineer Intern',
            'company': 'CCC Intelligence Solutions',
            'date': 'May 2023 – Current',
            'location': 'Chicago, IL',
            'responsibilities': [
                'Designed and implemented big data pipelines, ingesting data from various sources, processing it in ETL pipelines, and delivering cleaned data using parallel processing technologies such as Kubernetes and PySpark.',
                'Implemented daily, batch, and real-time data processing pipelines using Apache Airflow for orchestrating workflows.',
                'Built an innovative internal tool with a custom hashing algorithm and database/application design, resulting in an 85% improvement in data processing time.',
                'Leveraged AWS services including EMR clusters and Lambda functions to create robust data pipelines transforming and delivering data to data warehouse.',
                'Automated the collection and analysis of performance data from each pipeline, developed a web application for unified and comprehensive pipeline monitoring, and deployed it using Docker and Kubernetes.'
            ]
        },
        {
            'role': 'Data Scientist Intern',
            'company': 'Division Of IT, University of South Carolina',
            'date': 'May 2022 – April 2023',
            'location': 'Columbia, SC',
            'responsibilities': [
                'Deployed automated data pipelines on Azure Cloud, cleansing and evaluating datasets via REST-API for real-time Tableau dashboard insights.',
                'Collaborated on ETL tasks, ensuring data integrity and pipeline stability.',
                'Built containerized applications using Docker for seamless, isolated execution environments.'
            ]
        },
        {
            'role': 'Software Engineer Intern',
            'company': 'Billzio Co',
            'date': 'Sep 2020 – July 2021',
            'location': 'San Francisco, CA',
            'responsibilities': [
                'Designed web applications and endpoints using Flask framework.',
                'Solved financial business problems using data-driven approaches.',
                'Implemented machine learning automation, increasing user interaction by 20%.',
                'Managed PostgreSQL databases, including migration and schema design.'
            ]
        }
    ]

    education = [
        {
            'degree': 'Master of IT',
            'institution': 'University of South Carolina',
            'graduation_date': 'Dec 2024',
            'details': 'Research: Optimizing big data pipelines in healthcare using machine learning, focusing on bioinformatics applications.'
        },
        {
            'degree': 'Bachelor of Science: Mechanical Engineering',
            'institution': 'Azad University of Tehran',
            'location': 'Tehran'
        }
    ]

    certificates = [
        'AWS Cloud Practitioner',
        'ML on Big Data, IBM (Coursera)',
        'Data Structure, UCSD (Coursera)',
        'Data Science in healthcare'
    ]

    skills = {
        'Cloud Services': 'AWS, Azure, Google Cloud',
        'Big Data Engineering': 'ETL, ELT, Data pipeline design',
        'Data Pipeline Tools': 'Python, Docker, Kubernetes, EMR, Lambda, PySpark, Airflow',
        'Programming Languages': 'Python, Pyspark, Scala, SQL, NoSQL, Java',
        'Data Visualization': 'Tableau, Power-BI, Plotly, Seaborn',
        'Software & Tools': 'PostgreSQL, MongoDB, Presto, Dbeaver, Postman, Hive, Git',
        'Machine Learning Technologies': 'Scikit-learn, Pytorch, Tensorflow'
    }
    
    projects = [
        {
            'name': 'Big Data Pipeline for Healthcare Data Integration',
            'description': 'Designed and implemented a big data pipeline for integrating diverse healthcare datasets, including patient records, medical imaging, and lab results. The pipeline leveraged Apache Spark for distributed data processing, optimized ETL processes, and ensured HIPAA compliance. Containerized the entire pipeline using Docker, and deployed it on a Kubernetes cluster, which allowed for scalable and resilient data processing. This setup resulted in a 40% reduction in data processing time and improved data accessibility for healthcare professionals.',
            'technologies': 'Apache Spark, Python, Hadoop, Docker, Kubernetes, AWS EMR, S3, Redshift'
        },
        {
            'name': 'Real-Time Data Processing System for Insurance Claims',
            'description': 'Developed a real-time data processing system to handle high-frequency insurance claim data. Implemented using Apache Kafka and PySpark, the system ingested and processed data streams, providing near real-time insights and anomaly detection. The deployment was handled through Docker containers orchestrated by Kubernetes, ensuring high availability and scalability. This project reduced latency in data processing by 60%, enhancing decision-making capabilities for claims managers.',
            'technologies': 'Apache Kafka, PySpark, Docker, Kubernetes, AWS Lambda, S3, PostgreSQL'
        },
        {
            'name': 'Automated Data Pipeline for Financial Analytics',
            'description': 'Built an automated data pipeline for processing and analyzing large volumes of financial transaction data. The pipeline was designed to handle both batch and real-time data, with automated anomaly detection and alerting mechanisms. The pipeline was containerized using Docker and deployed on a Kubernetes cluster, facilitating easy scaling and management. This deployment improved data processing efficiency by 50%.',
            'technologies': 'Python, Docker, Kubernetes, AWS Lambda, Redshift, S3, PostgreSQL'
        }
    ]

    context = {
        'personal_info': personal_info,
        'projects': projects,
        'experience': experience,
        'education': education,
        'certificates': certificates,
        'skills': skills
    }
    return render(request, 'main/resume.html', context)

def new_page(request):
    # New blank page view
    return render(request, 'main/new_page.html')

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Construct the email
        subject = f"Message from {name}"
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        recipient_list = [settings.EMAIL_HOST_USER]  # Your email address
        send_mail(subject, email_message, email, recipient_list)

        return redirect('home')  # Redirect to a thank you page or home page
    return render(request, 'main/home.html')



def dashboard_view(request):
    # Query data from the database
    newyork_data = newyorknearby_trends.objects.all()
    sandiego_data = sandiegonearby_trends.objects.all()
    sanfrancisco_data = sanfrancisconearby_trends.objects.all()

    # Get field names excluding 'month'
    newyork_fields = [f.name for f in newyorknearby_trends._meta.fields if f.name != 'month']
    sandiego_fields = [f.name for f in sandiegonearby_trends._meta.fields if f.name != 'month']
    sanfrancisco_fields = [f.name for f in sanfrancisconearby_trends._meta.fields if f.name != 'month']


    # Pass data to the template
    context = {
        'newyork_data': newyork_data,
        'sandiego_data': sandiego_data,
        'sanfrancisco_data': sanfrancisco_data,
        'newyork_fields': newyork_fields,
        'sandiego_fields': sandiego_fields,
        'sanfrancisco_fields': sanfrancisco_fields,
    }
    return render(request, 'main/dashboard.html', context)

