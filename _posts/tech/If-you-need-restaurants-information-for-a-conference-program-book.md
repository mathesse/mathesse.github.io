---
layout: post
title: If you need restaurants information for a conference program book
category: TECH
tags: r api
keywords: TECH
description:

---
# <font color="#ff5f2e"><center>If you need restaurants information for a conference program book...</center></font>

May 10, 2018

## Story

Professor A: "Would you mind generating a list with local restaurants? We would like to put it on the conference program book. If there is a map and a table, that would be the best!"

"Something like this..."

- http://www.nclaonline.org/sites/default/files/images/conference/restaurantdowntown.jpg
- https://arlisna.org/vra-arlis2011/about.html

## Lazy as I am… would never do manually insert:)

The basic idea is to grasp information from Yelp or Google with **location** information, and some other factors, if interested.

Feels that yelp has more review counts and thus I chose **Yelp**.

### Yelp API could do this

Yelp API has Business Endpoints including [Business Search](https://www.yelp.com/developers/documentation/v3/business_search) and [Business Details](https://www.yelp.com/developers/documentation/v3/business), which could satisfy my needs.

- To use Yelp Fusion API, you need [API Keys](https://www.yelp.com/developers/documentation/v3/authentication#where-is-my-client-secret-going) since March 1, 2018 since the API no longer uses OAuth 2.0 for requests and moved over to only API Keys. All you need to do is to fill a form indicating that you are creating an app and that's it. Once done, you could find the API Keys on [Manage App](https://www.yelp.com/developers/v3/manage_app).
- The request is simple `GET https://api.yelp.com/v3/businesses/search`. Yelp has help page [Business Search](https://www.yelp.com/developers/documentation/v3/business_search) and you could find query parameters and specify what will be your responses.
- Common query parameters include
  - term: if you search for `term = ""` then API gives results for all business, not only limited to restaurants. I found this tricky and weird since API actually returns nothing when I indicate `term = "food"` or `term = "restaurants"`, and `term = ""` only returns food-related business in my interested area.
  - categories: well, if you search for `categories = "latin"` you will get nothing. Probably due to the fact that the categories is a list.
  - location OR latitude + longitude: I feel lat+lon might be easier to use, since you could easily find the values from [a converter using address](https://www.latlong.net/convert-address-to-lat-long.html).
  - radius: unit is meter. How it is from central location. Largest possible value is 40000 meters.
  - limit: 50 maximum one time, but you could combine the datasets. Pay attention that the API has a limit as well.
  - sort_by: by default it is best_match, however I feel more comfortable using review_count and rating. Distance is also a possible option.
  - price: 1($)-4($$$$).
- Common responses could include
  - name
  - categories (use title for display): returns a list.
  - phone (use display_phone)
  - distance
  - is_closed: Yelp has information of business that are permanently closed.
  - location: address, city, state, zip code: zip code is necessary if you assume your potential readers are going to use Map apps! A lesson from life!
  - rating
  - review counts
  - transactions: this is a list! When you are going to write results to excel, make sure to convert it to string.

## Sample code

```R
# restaurant info #
# --------------- #
require(tidyverse)
require(httr)
# build the url for query, use API key instead of token from March, 2018
# function to parse and format the data and do the search
yelp_business_search <- function(term = NULL, 
                                 location = NULL, 
                                 latitude = NULL, longitude = NULL,
                                 categories = NULL, 
                                 radius = NULL, 
                                 limit = 10, 
                                 price = NULL, 
                                 sort_by = NULL,
                                 apikey = NULL) {
  
  yelp <- "https://api.yelp.com"
  url <- modify_url(yelp, path = c("v3", "businesses", "search"),
                    query = list(term = term, 
                                 location = location, 
                                 latitude = latitude, 
                                 longitude = longitude, 
                                 limit = limit, 
                                 radius = radius, 
                                 categories = categories,
                                 price = price, 
                                 sort_by = sort_by))
  res <- GET(url, add_headers('Authorization' = paste("bearer", apikey)))
  results <- content(res)
  
  yelp_httr_parse <- function(x) {
    
    parse_list <- list(id = x$id, 
                       name = x$name, 
                       rating = x$rating, 
                       review_count = x$review_count, 
                       latitude = x$coordinates$latitude, 
                       longitude = x$coordinates$longitude, 
                       address1 = x$location$address1, 
                       city = x$location$city, 
                       state = x$location$state, 
                       distance = x$distance,
                       zip_code = x$location$zip_code,
                       phone = x$phone,
                       display_phone = x$display_phone,
                       price = x$price,
                       transactions = x$transactions,
                       is_closed = x$is_closed,
                       categories = x$categories
                       )
    
    parse_list <- lapply(parse_list, FUN = function(x) ifelse(is.null(x), "", x))
    
    df <- data_frame(id=parse_list$id,
                     name=parse_list$name, 
                     categories = parse_list$categories,
                     rating = parse_list$rating, 
                     review_count = parse_list$review_count, 
                     address1 = parse_list$address1, 
                     distance= parse_list$distance,
                     zip_code = parse_list$zip_code,
                     phone = parse_list$display_phone,
                     price = parse_list$price,
                     transactions = parse_list$transactions,
                     is_closed = parse_list$is_closed,
                     city = parse_list$city, 
                     state = parse_list$state,
                     latitude=parse_list$latitude, 
                     longitude = parse_list$longitude
                     )
    df
  }
  results_list <- lapply(results$businesses, FUN = yelp_httr_parse)
  payload <- do.call("rbind", results_list)
  payload <- payload %>%
    filter(grepl(term, name))
  
  payload
}
# result
results <- yelp_business_search(latitude = [your-lat],
                                longitude = [your-lon],
                                term = "",
                                radius = 3000, 
                                limit = 50, 
                                sort_by = "review_count",
                                apikey = "[your-api-keys]"
)
# write to file
results$categories <- vapply(results$categories, paste, collapse = ", ", character(1L))
results$categories = sub('.*,', '', results$categories)
results$transactions = as.character(results$transactions)
write.csv(results[,-1], "[your-file-name].csv")
```

### Sample output

![](/public/img/posts/20180510/20180510-yelp-api.png)



*With the data, now you could plot the map and generate kable tables:)*



## Reference

- [An R package to search for businesses at a location](https://github.com/walshc/YelpAPI): this package is written before  Yelp moves to API Keys from tokens, so you could download the raw code and manually adapt it.
- [Using the Yelp API with R](https://billpetti.github.io/2017-12-23-use-yelp-api-r-rstats/): very useful sample code, however also written before API keys, so minor adaptation. 





