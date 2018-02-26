## JupyterLab

You’ve probably have heard of the debate over why one should use Python 2 over Python 3. Maybe some of you may be confused as to which one you should use — Python 2 or Python 3? Well, scientific Python projects are officially sunsetting Python 2 [by 2020](http://python3statement.org/). And the [NumPy project](https://github.com/numpy/numpy/blob/master/doc/neps/dropping-python2.7-proposal.rst) is phasing out support for Python 2. For those who are new developers, it might be wise to learn Python 3. Python 3 is a better written software that takes care of the bugs that were in Python 2. Also, most Linux distributions have Python 3.x already installed, and all have it available for end-users.However, there are disadvantages of using Python 3. For example, there are more third party libraries for Python 2 than for python 3, especially for machine learning algorithms. But, over time that will change as more of the packages will be written or rewritten for Python 3. 

This debate relates to the recent news from JupyterLab. Should one use Jupyter notebook or JupyterLab. As some of you may know, we do most of our analysis on Jupyter notebook, but we’ll be adopting JupyterLab too. 

So the classic Jupyter notebook as you may know is about, at this point, more than just notebooks. In addition to having notebooks, Jupyter has a text editor, an in-browser terminal, a full-blown file browser, and all of these different things are needed for doing interactive computing with data. Whether you're doing data science or scientific computing or machine learning, usually you want to run the computation where your your data is and that's often not in your laptop. So a lot of our users are starting to run Jupyter in a context, where the data is not on their laptop -- they're connected to some remote system. At that point the Jupyter notebook is the user interface not just writing that code, but to the entire system. So having the file browser with a terminal and all these other things become really important building blocks for interactive computing. 

But if you think about the RStudio workflow, the classic Jupyter notebook is not the only way of assembling and integrating these different building blocks. Traditionally, Rstudio allowed you to just edit standalone R scripts and then select blocks of R code to run them in something like a code console. It's a different workflow, and it still uses the same abstractions for interactive computing of having a place to type code, output, etc. but it's a different way of assembling those building blocks.

Jupyter merges both IDE and notebook functionalities. It’s mostly convenient when you work on multiple notebooks or project, as it allows you to concentrate all your python work under a single tab. It’s nothing that will change your life, but think of it like Jupyter notebook plus a better user interface. In addition, there are more features available only in JupyterLab. For example, within the JupyterLab environment, you can: access files without having to go on another page, open a raw data file like .csv file, and open a terminal, making development and software maintenance much more convenient. The documentation for JupyterLab can be found [here](https://media.readthedocs.org/pdf/jupyterlab/latest/jupyterlab.pdf). 

<p align="center">
  <img src="src-jupyterlab-blog/blog-jupyterlab-1.png" width="1500"/>
</p>




