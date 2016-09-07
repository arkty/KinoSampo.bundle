TITLE = 'Swap'
PREFIX  = '/video/swap'

BASE_URL = 'http://kino.sampo.ru/movie'

def Start():
  HTTP.CacheTime = CACHE_1HOUR
  ObjectContainer.title1 = 'Swap'

@handler(PREFIX, TITLE)
def MainMenu():
  oc = ObjectContainer()
  # Hard coded the links offered under the Watch pull down list
  oc.add(DirectoryObject(key=Callback(Categories, title='Series'), title='Series'))
  #oc.add(InputDirectoryObject(key = Callback(SearchOptions, title="Search"), title = "Search"))
  return oc


@route(PREFIX + '/categories')
def Categories(title):

  oc = ObjectContainer(title2=title)

  # local_url = '%s/%s' %(BASE_URL, title.lower())
  # html = HTML.ElementFromURL(local_url)

  # for category in html.xpath('//div[@class="category_grid"]//a'):

  #   title = category.xpath('.//p[@class="title"]/text()')[0]
  #   category_url = BASE_URL + category.xpath('./@href')[0]
  #   thumb = category.xpath('.//img/@src')[0]

  #   oc.add(DirectoryObject(
  #     key = Callback(CategorySections, title=title, url=category_url, thumb=thumb),
  #     title = title,
  #     thumb = Resource.ContentsOfURLWithFallback(url=thumb)
  #   ))
