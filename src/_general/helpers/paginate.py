def get_page_items(page):
    page_items: dict = {'total': page.total,
                        'page': page.page,
                        'pages': page.pages,
                        'per_page': page.per_page,
                        'items': []}

    for item in page.items:
        dict_item = {}

        for key, value in item.__dict__.items():
            if not key == '_sa_instance_state' and not key == 'password_hash':
                dict_item[key] = value

        page_items['items'].append(dict_item)

    return page_items
