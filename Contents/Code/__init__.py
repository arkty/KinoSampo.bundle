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
  oc.add(DirectoryObject(key=Callback(Categories, title='Categories'), title='Categories'))
  #oc.add(InputDirectoryObject(key = Callback(SearchOptions, title="Search"), title = "Search"))
  return oc


@route(PREFIX + '/categories')
def Categories(title):

  oc = ObjectContainer(title2=title)
  oc.add(VideoClipObject(
            url = "http://storage14.swap.sampo.ru/%D0%A1%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D1%8B/%D0%97%D0%B0%D1%80%D1%83%D0%B1%D0%B5%D0%B6%D0%BD%D1%8B%D0%B5/%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F%20%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B3%D0%BE%20%D0%92%D0%B7%D1%80%D1%8B%D0%B2%D0%B0%20%28The%20Big%20Bang%20Theory%29/%D0%A1%D0%B5%D0%B7%D0%BE%D0%BD%208/The.Big.Bang.Theory.S08E01.HDTVRip.720p.Kuraj-Bambey.%5Bqqss44%5D.mkv",
            title = "The Big Bang Theory",
            summary = "Some summary",
            duration = "10:20",
            thumb = Resource.ContentsOfURLWithFallback("http://kino.sampo.ru/resize/poster/9/7309/w210h290.jpg?1463393951")
        ))

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
