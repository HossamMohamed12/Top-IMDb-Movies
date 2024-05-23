import json

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags
import json

def process_rating_count(value):
    return value+'/10'

def get_rank(value:str):
    return (value.rsplit('_'))[-1]

class TopMoviesItem(scrapy.Item):
    rank = scrapy.Field(
         input_processor=MapCompose(get_rank, int),
         output_processor=TakeFirst()
    )
    title = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    genres = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip)
    )
    release_date = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip, int),
        output_processor=TakeFirst()
    )
    age_rating = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    duration = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    rating = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip, process_rating_count),
        output_processor=TakeFirst()
    )
    reviews_count = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip,),
        output_processor=TakeFirst()
    )

d = 'https://www.imdb.com/title/tt0167261/?ref_=chttp_i_12'

print ((d.rsplit('_'))[-1])