This python script counters an import/export problem of magento products in magento 1.9.x. By default, magento exports the configurable product rows first and the associated (simple) products after. This results in failure in linking between them while importing. 

This script addresses this issue by rearranging the rows in the csv file accordingly.
