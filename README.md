# FEA Result Processing

A python program that would assist the engineer with processing results and providing a way to see the development of the product.

## How to use

-- update when get in head space!!

## Inspiration for build

### Current Process

Current way to process the result in the FEA group. The Engineer would add the results to an Spreadsheet. Once file is updated with result then the Person In Charge (PIC) would need to tailor spreadsheet for the the request. Then would need to send out a screen shot of the values to the group.

### Problem with Process

First off there is to much handling the result data. The PIC would have to copy paste, and hide specific row and column to keep the updates to the group simple.

Second is that currently all result and model data are stored in "master" spreadsheet. This method does not provide a good way of seeing the overall process of product development.

## Proposal

The most important part currently is to get something in the wild. Product development was ramping up and I wanted to start tracking to see if there was any issue or any other features that could provide assistance to the PIC.

## Program Build Steps

1. Template file, to hold the info and results of model that is to be validated
2. Watcher file, A script to watch for updates to the template file. This would fire off the rest of the process
3. Add serialization of results data to database (sqlite3)
4. Retrieve target results and the model that cm model is base on
5. Calculate stiffness percentage to target, allow easier way to determine if model is OK
6. Structure the table for the spreadsheet
7. Provide a way for the PIC to customize the values output in spreadsheet
8. Save the file in the similar format that would replicate the PIC's report.

### Python Build Process

Main objective was to have the PIC to not have a large buy-in to use the program. Keeping the within the spreadsheet ecosystem seems like the most logical answer. By creating a template for the main entry way creating would allow the Engineer to operate in a familiar format. An added benefit to the template file is that a Python script can be create to watch file and then fire off the process.

When the watcher indicates an update to the template file by a save. Program will take the data save to the file an start to process it to save to the database. The template file has two sections the top is information pertaining to the model ei.(weight, base model name, description). The lower half would be the the values of the load points. The result database is structure to be able to add more data if needed.

## Concerns / possible issues

- changing the template file keys for the database. since the DB need to know what column the values should be added to.

## Future Features

1.
