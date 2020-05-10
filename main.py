import o365_sharepoint_connector
login = input("Enter your O365 account: ")
password = input("Enter your O365 password: ")
site_url = input("Enter SharePoint site: ")
list_title = input("Enter SharePoint list title: ")


connector = o365_sharepoint_connector.SharePointConnector(login, password, site_url)
connector.authenticate()
list_byTitle = connector.get_list_by_title(list_title)
print(list_byTitle)
