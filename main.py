import o365_sharepoint_connector
login = input("Enter your O365 account: ")
password = input("Enter your O365 password: ")
site_url = input("Enter SharePoint site: ")
list_title = input("Enter SharePoint list title: ")


connector = o365_sharepoint_connector.SharePointConnector(login, password, site_url)
connector.authenticate()
list_byTitle = connector.get_list_by_title(list_title)


def print_list_properties(sp_list):
    """Return list properties"""
    print(
        "\nTitle:",                         sp_list.title,
        "\nId:",                            sp_list.id,
        "\nHidden: ",                       sp_list.hidden,
        "\nCreated: ",                      sp_list.created,
        "\nDescription: ",                  sp_list.description,
        "\nType: ",                         sp_list.entity_type_name,
        "\nLast item deleted date: ",       sp_list.last_item_deleted_date,
        "\nLast item modified date: ",      sp_list.last_item_modified_date,
        "\nLast item user modified date: ", sp_list.last_item_user_modified_date,
        )