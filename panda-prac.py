import pandas as pd

df=pd.read_csv("C:/Users/Admin/amazon.csv")
print(df.head(5))

print(len(df))
print(len(df.axes[1]))
print(df.shape)

dict={1:"audi",2:"bmw",3:"mercedes",4:"auto"}

df1=pd.DataFrame(dict,index=[1],columns=[1,2,3])
print(df1)


