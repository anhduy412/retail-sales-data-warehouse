SELECT * FROM [dbo].[DataCoSupplyChainDataset]

SELECT count(distinct Order_Item_Id) FROM [dbo].[DataCoSupplyChainDataset]

select [Order_City], [Order_Country], [Order_State], [Order_Region] from [dbo].[DataCoSupplyChainDataset]
group by [Order_City], [Order_Country], [Order_State], [Order_Region]

select Customer_Id
from [dbo].[DataCoSupplyChainDataset]
order by [Customer_Id];