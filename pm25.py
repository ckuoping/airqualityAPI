class PM25:
    def __init__(self, data):
        # self.id=data['SiteId']
        self.name = data['SiteName']
        # self.city=data['County']
        # self.itemId=data['ItemId']
        # self.itemName=data['ItemName']
        # self.itemEngName=data['ItemEngName']
        self.unit = data['ItemUnit']
        self.date = data['MonitorDate']
        self.data = data['Concentration']
