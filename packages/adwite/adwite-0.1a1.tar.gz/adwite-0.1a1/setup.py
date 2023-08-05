from setuptools import find_packages, setup

doc = """# Adwite
## English
> GUI extension library
>> tkadw (tkinter extension)
> 
>> gtkadw (pygobject extension)
>
>> qtadw (pyside6 extension)

> Library info
>> _Version_ `0.1 alpha1`
>
>> _Authors_ `xiangqinxi`
>
>> _License_ `MIT License`
> 
>> _Website_ `https://adwite.netlify.app/`


## 简体中文
> GUI扩展库
>> tkadw (tkinter扩展)
> 
>> gtkadw (pygobject扩展)
> 
>> qtadw (pyside6扩展)

> 库信息
>> _版本_ `0.1 alpha1`
> 
>> _作者_ `向秦希`
> 
>> _许可证_ `麻省理工许可证`
> 
>> _文档_ `https://adwite.netlify.app/zh/`
"""

setup(
    name="adwite",
    version="0.1alpha1",
    author="XiangQinxi",
    author_email="XiangQinxi@outlook.com",
    description="GUI extension library",
    long_description=doc,
    long_description_content_type="text/markdown",
    python_requires=">=3",
    packages=find_packages(
        where=".",
        exclude=["doc"]
    ),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
