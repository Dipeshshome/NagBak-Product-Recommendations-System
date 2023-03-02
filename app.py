import streamlit as st
import pickle
import pandas as pd


def recommend(products):
    product_index=product[product['xdesc_title']==products].index[0]
    distances=similarity[product_index]
    product_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_product=[]
    recommended_product_image=[]
    recommended_product_imagepath=[]
    for i in product_list:
        bizid=product.iloc[i[0]].bizid
        #imagepath=product.iloc[i[0]].xmainimage
        recommended_product.append(product.iloc[i[0]].xdesc_title+' '+product.iloc[i[0]].xmrp_title+' BDT')
        recommended_product_image.append(bizid)
        recommended_product_imagepath.append(product.iloc[i[0]].xmainimage)
    return recommended_product,recommended_product_image,recommended_product_imagepath


product_dict=pickle.load(open('products_dict.pkl','rb'))
product=pd.DataFrame(product_dict)

similarity=pickle.load(open('similarity.pkl','rb'))


st.subheader('Product Recommendation System - Nagbak')

selected_product_name = st.selectbox(
    'How would you like to be contacted?',
    product['xdesc_title'].values)

if st.button('Recommend'):
    recommendations,bizid,imagepath=recommend(selected_product_name)
    col1, col2, col3,col4,col5 = st.columns(5)   
    #col1=st.columns(1)

    with col1:
        id=str(bizid[0])
        st.text(recommendations[0])
    #.text(imagepath[0])  
        st.image("https://nagbak.com/archive/"+id+"/itemimages/"+imagepath[0])

    with col2:
        id=str(bizid[1])
        st.text(recommendations[1])
    #.text(imagepath[0])  
        st.image("https://nagbak.com/archive/"+id+"/itemimages/"+imagepath[1])

    with col3:
        id=str(bizid[2])
        st.text(recommendations[2])
    #.text(imagepath[0])  
        st.image("https://nagbak.com/archive/"+id+"/itemimages/"+imagepath[2])

    with col4:
        id=str(bizid[0])
        st.text(recommendations[3])
    #.text(imagepath[0])  
        st.image("https://nagbak.com/archive/"+id+"/itemimages/"+imagepath[3])  

    with col5:
        id=str(bizid[4])
        st.text(recommendations[4])
    #.text(imagepath[0])  
        st.image("https://nagbak.com/archive/"+id+"/itemimages/"+imagepath[4])      


   

