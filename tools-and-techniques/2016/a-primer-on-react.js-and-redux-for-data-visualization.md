## A Primer on React.js and Redux for Data Visualization Professionals

I try to never take for granted that my background, like all our backgrounds, is unique.  Two data scientists can easily find they have nothingin common.  For me, this is an opportunity to help others bridge the various gaps between the knowledge they currently have and what's within arm's reach.

I've gotten excited about two technologies recently that I think data visualization people should be aware of.

The first is React.js.  It's a framework started by Facebook which has dramatically accellerated the speed at which people can develop web applications and the complexity those applications can achieve without incurring a significant amount of technical debt or code that is over-opinionated to the point that new people can't work on it.

The second is Redux, which I admittedly know only the basics of, but that should be fine for this post which only attempts to share the basics with people from the data visualization world looking to get started.  I'll be discussing Redux is a separate, future blog post.

I'll assume you begin with a knowledge of HTML, CSS, and D3.

React.js makes web development work in an intuitive way.  Everything in React is a Component.  Visit any website you'd like and your mind should find it pretty easy to divide up the page into sections - header, menu, comment box, shopping cart, main body, etc.  Every component is defined uniquely in it's own file.

Let's take a look at one of the Components on [dataskeptic.com](http://dataskeptic.com).

<script src="https://gist.github.com/kylepolich/15e8eaa77137fb6826d0329103f57968.js"></script>

There are three methods: constructor, onChange, and render.  Let's explore each.

The `constructor` should be relatively obvious to anyone with the basics of object oriented programming.  What's unique here is that we're defining a variable called `state` which is special in React.js.  Every Component has a state, and the state is a full description of the Component.  Once the Component is rendered, nothing further needs to happen unless the state changes.  The beautify of React.js is that it will take care of all the updates for us.  We just need to define how to render the Component and then maintain it's state.  There's no need to worry about doing the updates ourselves.  We're actually going to stop using `state` when I discuss Redux in my next blog post.  However, it's useful to get started using `state`, even if you migrate later.  It helps with the intuition of how to use React.js.

The `render` method needs to return a single tag, although it can have inner tags.  Your hello world might look something like this:

	render() {
		return (
			<div className='hw-container'>Think skeptically of and with data</div>
		)
	}

I often find myself making a container to keep this simple.  Notice I'm using `className` and not `class`.  I'll spare you the details of why I did this, just run with it.  It's the React way :)

The `render` method should output all your HTML to draw the component.  You can reference variable inside curly braces, like I did with `this.state.email`.  As a best practice, I think all your variables should pull directly from your state.  You might want to define them like this...

	render() {
		var name = this.state.shopping.department.display.name
		return <h1>{name}</h1>
	}

... for readability purposes.  You're not required to only pull from state, but I think you might be making a mistake to do something different.  Remember that the state should describe everything there is to know about your Component.

You can specify other components inline, for example:

	render() {
		return (
			<div className="site-container">
				<Header />
				<Menu />
				<MainSection isPaidMember={this.isPaidMember} />
				<Footer />
			</div>
		)
	}

Notice that my `MainSection` component has a passed in parameter.  Do this when a Component needs a value but does not "own" that value.  It can be accessed inside the `MainSection` component as `this.props.isPaidMember`.

Lastly, the `onChange` function is called when the input is changed.  One important thing about React.js is that you *must only* update the state using `this.setState()`.  Never do `this.state.foo = 'bar'` directly.  Don't ask questions, just do it.

### React.js for Data Visualization

For specifically working with data visualization, I believe React gives two main advantages.

First, it allows you to produce clearer and more readible code.  I find I'm able to return to projects weeks or months later and get back up to speed pretty quickly.  That was never the case in my non-React D3 work which tended to live in monolotic source files.

Second, it provides a nice separation of concerns.  You need to teach yourself to think in Components.  This comes very naturally.  With a well structured heirarchy of Components, you'll be able to issolate the area you want to improve more easily.  You should also encounter no side effects whatsoever, which I can't say about most of my Javascript/D3 "by hand" projects.

These are the more tangible benefits that make writing code easier.  React.js also does a few services that I've long since started taking for granted.  Primarily, this is around updating.  When responding to input, I use to have to think carefully about the required steps.  Where do I store the new values?  How do I update the bars / shapes on the image?  Do I have to retrieve some other bit of information from elsewhere in my code?  Do I need to inform any other parts of the project that I have updated something?

All those concerns disappear in React.  Get some event (user input or perhaps a timer event), update the state, and forget about the rest.

Additionally, writing things in the React way allows me to separate out actions on the visualization from the rendering of the components themselves.  This means that if I have a logical error (wrong value showing), I need to inspect the `state` and debug the update functions.  If I have an alignment issue or ugly axis, I need to check the render components.  I find this separate makes productivity jump up significantly.

Lastly, React gives me a strong framework for exploiting encapsulation.  If my complex visualization is built up from some components, I can lock myself in a room and focus on building just one of the simple pieces.  I can make it awesome and flawless without worrying about the big picture.  It only needs to respond to the `props` it's given and maintain it's own state.

### Conclusions

I'm very excited about using React.js for my own data visualizations and I think it can help make lots of other people more productive as well.

In my opinion, there are two major limitations, both of them specific to React.js.

First, adding navigation (like a menu) to your project is suprisingly difficult.  Really?  Yup.  You'll need to use the react-router, which has had at least two major versions that are not particularly compatible with one another.  The tutorials out there aren't great at this time, but once you get it working, the router does it's job well.  It can be a pain for setup, though.

Second, React.js is bad for SEO out of the box, and you have to take extra steps to fix it.  By default, the code is bundled into a nice minified Javascript library.  When one points there browser at a React.js page, this script is downloaded and run.  It then self populates the entire web site.  This is a seamless and typically fast experience for the user.  However, when you "view source" of the page, you'll find absolutely no content - just a script tag that does all the magic after the page is "loaded".  This is going to make your content invisible to almost all crawlers.  I've been told that Google does run Javascript and *might* be able to crawl your React.js site.  Sadly, I found that this was not the case when I used the Google web developer tools.  It appeared that the Google Crawler saw only a blank site.  I had to take some extra steps to provide server side rendering with Express.js and some clever caching to make my site fast and crawlable.  This was an unpleasant suprise at the end of project I thought was nearly complete.  Yet, since I've done a lot of the heavy lifting here, you might want to check out the [dataskeptic.com repo on github](https://github.com/data-skeptic/dataskeptic.com) for a relatively minimal example of how to set it up.

I have not by any means taught you everything about React.js here.  However, I hope this is enough to get started using it for data visualization purposes.
