#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Function to download and extract datasets
def download_and_extract(url, filename, extract_dir):
    print(f"Downloading {filename}...")
    with requests.get(url, stream=True) as response:
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print(f"{filename} downloaded.")
    
    print(f"Extracting {filename}...")
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"{filename} extracted.")


# In[1]:


def add(num):
    return num+1


# In[ ]:




