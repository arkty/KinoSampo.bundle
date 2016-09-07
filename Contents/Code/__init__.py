TITLE = 'Swap'
P_SERIES  = '/swap/series'

def Start():
  HTTP.CacheTime = CACHE_1HOUR
  ObjectContainer.title1 = 'Kino Sampo'

@handler(P_SERIES, TITLE)
def MainMenu():

  oc = ObjectContainer()
  # Hard coded the links offered under the Watch pull down list
  oc.add(DirectoryObject(key=Callback(SectionSort, title='Staff Picks', url=STAFF_PICKS), title='Staff Picks'))
  oc.add(DirectoryObject(key=Callback(Categories, title='Categories'), title='Categories'))
  oc.add(DirectoryObject(key=Callback(SubMenu, title='Channels', url=CHANNELS), title='Channels'))
  oc.add(DirectoryObject(key=Callback(SubMenu, title='Groups', url=GROUPS), title='Groups'))
  oc.add(InputDirectoryObject(key = Callback(SearchOptions, title="Search"), title = "Search"))
  return oc
