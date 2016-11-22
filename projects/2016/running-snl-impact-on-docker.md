## Running SNL Impact on Docker

I'll spare you a long story of clenched fists and flowing expletives and simply say that getting the `CausalImpact` library running can be quite tricky due to some dependencies that do not gracefully install in all situations.

As one ought to do when concerned with a fragile configuration problem, we turned to Docker.  It was simple to write a Dockerfile that properly configured an Ubuntu system to run our Shinyapp, even though we couldn't get it to run on the ubiquitous [shinyapps.io](shinyapps.io)!

If you'd like to try our code, you need to first have `git` and `docker` installed.  Next, clone our library and build the image it contains.

---
$ git clone https://github.com/data-skeptic/CausalImpact.git
$ cd CausalImpact/
$ docker build .
---

This will create a Docker Image that is properly configured to run our app and answer on port 3838.  Make a note of the imageID that is returned at the very end.  I got `Successfully built c7d816670255`.

If you'd like to try making some changes, you can fork our repository, and replace our repo with yours in the Dockerfile to get switch over to your version in one line of code.

When you're ready to run things, run the docker with the command below.

```
$ docker run -p 3838:3838 c7d816670255
```

That's all it takes to get things running.  So long as you leave that Docker container running, the Shinyapp will be active.  I chose port 3838 as the port I wanted to have it answer on.  By adding the parameter `-p 3838:3838`, I'm asking docker to map that open 3838 port of the container to my local machine so that I can access it in my normal browser by visiting [http://localhost:3838/](http://localhost:3838/).

If you make an interesting improvement or add a cool feature, we'd be interested in seeing your Pull Request.
