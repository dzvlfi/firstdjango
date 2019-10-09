# FIRSTDJANGO

Before you can use Django, you’ll need to get it installed. We have a complete installation guide that covers all the possibilities; this guide will guide you to a simple, minimal installation that’ll work while you walk through the introduction.
ref: ``https://docs.djangoproject.com/en/2.2/intro/install/``


# Django Description
Django is a widely-used Python web application framework with a "batteries-included" philosophy. The principle behind batteries-included is that the common functionality for building web applications should come with the framework instead of as separate libraries.
For example, authentication, URL routing, a template engine, an object-relational mapper (ORM), and database schema migrations (as of version 1.7) are all included with the Django framework. Compare that included functionality to the Flask framework which requires a separate library such as Flask-Login to perform user authentication.
The batteries-included and extensibility philosophies are simply two different ways to tackle framework building. Neither philosophy is inherently better than the other one.

That being said, why should you use Python in the first place? Why not one of the many other popular languages out in the wild like Ruby or PHP? Well, with Python you get the following awesome benefits:
1. Easily readable syntax.
2. Awesome community around the language.
3. Easy to learn.
4. Python is useful for a myriad of tasks from basic shell sripting to advanced web development.

### Django Pros and Cons
**The following pros of Django:**
1. Batteries included - ready for your MVP
Django helps developers by speeding up the development process. 
2. Security
Django includes prevention of common attacks like Cross-site request forgery (CSRF) and SQL Injections.
3. Python inside
Cjango inherit all Python's benefit
**The following cons of Django:**
1. Speed
Django offers its own benchmarks to check the speed of internals and spot all bottlenecks.
2. Lack of convention
Django ecosystem's relying on configuration is a common practice for the Python ecosystem.
3. Not always the right choice
Always pick the best tool for the job. Django may not be the right choice for really small sites, like static one-pagers or microservices - it this case you may want to use Flask.
