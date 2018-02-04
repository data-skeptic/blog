---
title: On Brewing Beer-in-Hand Data Science
author:
  name: Amanda Dobbyn
  email: amanda.e.dobbyn@gmail.com
  twitter: dobbleobble
output:
  html_notebook:
    toc: true
    theme: yeti
  pdf_document:
    keep_tex: true
    toc: false
  github_document:
    
    toc: true
# output:
#   html_document:
#     keep_md: true
#     toc: false
#     theme: yeti
#   github_document:
#     toc: true
#   pdf_document:
#     keep_tex: true
#     toc: false
editor_options: 
  chunk_output_type: inline
---




```
## Error: package or namespace load failed for 'dobtools'
```

```
## Error in library(feather): there is no package called 'feather'
```

```
## Error in library(emo): there is no package called 'emo'
```

```
## Error in eval(expr, envir, enclos): could not find function "read_feather"
```

```
## Error in file(filename, "r", encoding = encoding): cannot open the connection
```





<br>

This past summer I spent a chunk of time doing some [beer-in-hand data science](https://github.com/aedobbyn/beer-data-science) on, well, beer data. After I gave a [talk](https://aedobbyn.github.io/beer-data-science/) on the analysis at the aptly-named Oktoberfest edition of RLadies Chicago, a few people were interested in getting ahold of some beer data for themselves. I hope to spread the wealth in this quick post by going through some of the get-off-and-running steps that I took to grab beer data from BreweryDB API and do a first bit of cleaning on it.

I'll give a little backstory on why I started diving into beer data, which you can feel free to skip if you're just interested in the data extraction and wrangling parts.

![pour](./img/pour.jpg)

### Backstory

One day after work shooting it with a coworker, [Kris](https://kro.ski/), we were supplied with beer and a whiteboard, which in my book is a failsafe great combination. I don't pretend to be a beer aficionado, but Kris is the real deal; in addition to being an excellent web developer, Kris and his girlfriend man the popular Instagram account [kmkbeer](https://ink361.com/app/users/ig-6733117611/kmkbeer/photos). Around this time, Kris had started building an app for rating beers on a variety of dimensions, so you could rate, say, [Deschutes's Fresh Squeezed IPA](https://www.beeradvocate.com/beer/profile/63/60330/) on maltiness, sweetness and a host of other dimensions. That way you could remember not just that it's a 4.5/5 stars but that it's pretty juicy, all things considered. 

The main sticking point -- and this is where the whiteboard markers came out -- is that you'd want to be able to capture that a beer tasted smoky *for a porter* or was hoppy *for a wheat beer*. That's important because a very hoppy wheat beer might be considred quite a mildly hopped IPA. At this point we started drawing some distributional density curves and thinking about setting priors for every style. That prior would be the flavor baseline for each type of beer, allowing you to make these types of "for a" distinctions on the style level.  

This is about when I started thinking about the concept of beer "styles" in general. You've got -- at the highest split -- your ales and your lagers, and then within those categories you've got pale ales and IPLs and kölschs and double IPAs and whatnot. The categories people typically recognize as beer syles.

![beer_network](./img/beer_network.jpg)

But: are styles even the best way of dividing up beers? Or is it just the easiest and most immediate thing we've got? Assuming that beers do necessarily fit well into styles is a bit circular; we only have the style paradigmn to work off of so, if we're tasked with classifying a beer we're likely to reach for style as an easy way to bucket beers.

This brought me to thinking about clustering, of course. If styles <em>do</em> define the beer landscape well then, I figured, styles should match up with clusters pretty well. If they don't, well, that would be some evidence that the beer landscape is more of an overlapping mush than a few neat, cut-and-dry buckets and that maybe some stouts are actually closer to porters than they are to the typical stout, or whatever the case may be.

So! Where to get the data, though. The usual question. Well, Kris had his beers from an online database called [BreweryDB](http://www.brewerydb.com/developers), so, armed with a URL and a question I was interested in, I decided to check it out. 

### Getting Data

BreweryDB offers a RESTful API; what that means is that once you've created an API key [^1], you can hand that key over in a URL with query parameters and receive data back. The one caveat here is you won't get everything the API has to offer without creating a [premium](http://www.brewerydb.com/developers/premium) key ($6 a month); once you do, you'll get unlimited requests and a few extra endpoints beyond what you get at the free tier. 

![get_beers](./img/get_beers.jpg)

A look through the [BreweryDB API documentation](http://www.brewerydb.com/developers/docs) shows how you should structure your request in order to be handed back the data you want. You can get that data back as JSON (the default), XML, or serialized PHP. We'll be asking for JSON. If you're requesting data on a single beer, you'd supply a URL that contains the endpoint `beer`, the beer's ID, and your key like so:  `http://api.brewerydb.com/v2/beer/BEER_ID_HERE/?key=/YOUR_KEY_HERE`.

If you entered such a URL in the browser, the response looks like:

&nbsp;

![got_a_beer](./img/got_a_beer.jpg)

&nbsp;

That's beer data! But not that useful yet. We want to take that JSON and fit it into a dataframe. To do that, I turned to the excellent `jsonlite` package, which has a few functions for converting from JSON to R objects (generally lists) and vice versa. The main function we'll need is `fromJSON()`. Underneath `jsonlite` is are the `httr` and `curl` packages that allows you to construct HTTP requests in a straightforward way; what `fromJSON()` in particular does is take a URL, write a GET request for you, and give you back the reponse as a nested list.

To get our feet wet, we can generalize our URL write a little function that takes a beer ID and returns a nested list of data.




Okay so now we can reqeust a given beer by its ID:


```
## Error in paste0(base_url, "/beer/", id, "/", key_preface, key): object 'key' not found
```


&nbsp;

If we wanted to go back to JSON we can take a list like that and, you guessed it, use `toJSON()`:


```
## Error in paste0(base_url, "/beer/", id, "/", key_preface, key): object 'key' not found
```

&nbsp;


BreweryDB's got several endpoints that take a single parameter, an ID, just like the beer endpoint that we based our function on. I wanted a function for each of these endpoints so I could quickly take a look at the structure of the data returned. Rather than construct them all by hand like we did with `get_beer()`, this seemed like a good time to write a function factory to create functions to GET any beer, brewery, category, etc. if we know its ID.

First, a vector of all the single-parameter endpoints:




We'll first write a generic function for getting data about a single ID, `id` from an endpoint `ep`. 




Then we use a bit of functional programming in `purrr::walk()` and `purrr::partial()` to create `get_` functions from each of these endpoints in one fell swoop.





What's happening here is that we're piping each endpoint through `assign()` as the `.x` argument. `.x` serves as both the second half of our new function name, `get_<ep>`, and the endpoint argument of `get_()`, which we defined above (that is, the `ep` argument in the `fromJSON()` call). This means we're using the same word in both the second half of our newly minted function name and as its only argument.
(`assign` is the same thing as the usual `<-` function, but lets us specify an environment a little bit easier.)

Now we have the functions `get_beer()`, `get_brewery()`, `get_category()`, etc. in our global environment so we can do something like:


```
## Error in paste0(base_url, "/", ep, "/", id, "/", key_preface, key): object 'key' not found
```


Bam.

This is good stuff for exploring the type of data we can get back from each of the endpoints that take a singe ID. However, for this project I'm mainly just interested in beers and their associated data. So after a bit of poking around using other endpoints, I started thinking about how to build up a dataset of beers and all their associated attributes that might reasonably relate to their style.

<br>

### Building the Dataset

So since we're mostly interested in beer, our main workhorse endpoing is going to be `beers`. 

![grab_all_beers](./img/grab_all_beers.jpg)

The next challenge is how best to go about getting all the beers BreweryDB's got. We can't simply ask for all of them at once because our response from any one call to the API is limited to 50 beers per page. We can specify page with the `&p=` parameter in the URL.

The strategy I took, implemented in `paginated_request()`, was to go page by page, ask for all 50 beers on the page and tack that page's data on to the bottom of the one before it.

Helpfully, the `numberOfPages` variable in each page of the response tells us what the total number of pages is for this particular endpoint; it's is the same no matter what page we're on, so we'll take it from the first page and save that in our own variable, `number_of_pages`. We know which page we're on from `currentPage`. So since we know which page we're on and how many total pages there are, we can send requests and unnest each one into a datataframe until we hit `number_of_pages`. We attach each of the freshly unnested dataframes to all the ones that came before it, and, when we're done, return the whole thing.

What the `addition` parameter of our function does is let you paste any other parameters onto the end of the URL. If you want it on, `trace_progress` tells you what page you're on so you can more accurately judge how many more funny animal videos I mean stats lectures you can watch before you've gotten your data back. (It's worth noting that this function isn't optimized for speed at all, so queue up those videos or speed it up a bit by pre-allocating memory or vectorizing it ☺️.)

![onward](./img/onward.gif)





You'll notice a little helper funciton inside the for loop called `unnest_it()`. I'll explain what that's doing.

Looking back at the structure of the data resulting from `get_beer()`, we've got a nested list with things like `abv`, and `isOrganic`. The goal is get that nested list into a dataframe with as few list columns as possible. (If you're not familiar, a list-col is a column whose values are themselves lists, allowing for different length vectors in each row. They are neat but not what we're here for right now.)

Some bits of the data that we want are nested at deeper levels than others. For example, `$data$style` contains not just the `name` of the style but also the style's `description`, its `shortName`, the typical minimum ABV in `abvMin`, etc.


```
## Error in paste0(base_url, "/beer/", id, "/", key_preface, key): object 'key' not found
```

In these cases, we really only care about what's contained in the `name` vector; I'm okay with chucking the style attributes.


```
## Error in paste0(base_url, "/beer/", id, "/", key_preface, key): object 'key' not found
```


We'll write a helper function to put that into code. What `unnest_it()` will do is go along each vector in the top level of the `data` portion of the response and, if particular list item we're unnesting has a `name` portion (like `$style$name`), it will grab that value and stick it in the appropriate column. Otherwise, we'll just take whatever the first vector is in the data response. (We only need to resort to this second option in one case that I'm aware of, which is glassware -- glassware doesn't have a `name`.)





Okay, so we run the thing and assign it to the object `beer_necessities`. 
<!-- (I meant to change the name a long time ago but now it stuck and changing it would almost certainly break more things than it's worth 🤷🏼‍♀️). -->



We ask for ingredients in our addition so we know which particular hops and malts are included in each beer. These were unnested using a similar procedure.

![such_taps](./img/such_taps.jpg)

Let's take a look at some of what we've got:


```
## Error in eval(expr, envir, enclos): object 'beer_necessities' not found
```

The three main "predictor" variables we've got are ABV, IBU, and SRM. They stand for alcohol by volume, International Bitterness Units, and Standard Reference Method, respectively. What they mean is: how alcoholic is the beer, how bitter is it, and what color is it on a scale of light to dark.



```
## Error in glimpse(beer_necessities): object 'beer_necessities' not found
```









