# Scrappier

Scrappier is a web scrapper which uses chrome in a headless mode. This library provides an easy-to-read syntaxis to navigate through the different elements and perform actions.

## Requirements

* python 3.8
* chrome driver installed in /usr/bin//usr/bin/chromedriver

## Instalation

`pip install scrappier`

## Basic usage

    from scrappier import Browser

    browser = Browser()

    cards = browser.where_class("card").get()

    for card in cards:
        span = card.where_tag_name("span").first()

        print(span.text())

## Available methods for browser

### width()

### build()

### resize(width:int, height:int)

### webdriver()

### screen(path:str)

### wait(seconds:int)

### visit(url:str)

### where_xpath(xpath:str)

### where_id(id:str)

### where_name(name:str)

### where_contain_text(name:str)

### where_class_name(name:str)

### where_tag_name(name:str)

### where_attribute()

## Available methods for ElementFinder

### until(seconds:int)

### get()

### first()

### where_xpath(xpath:str, driver, element=None)

### where_id(id:str, driver, element=None)

### where_contain_text(text, driver, element=None)

### where_class_name(name:str, driver, element=None)

### where_tag_name(name:str, driver, element=None)

## Available methods for Element

### enter()

### type(text:str)

### text()

### html()

### attribute(name:str)

### click()

### children()

### where_tag_name(name:str)

### where_attribute(attribute:str, value:str)

