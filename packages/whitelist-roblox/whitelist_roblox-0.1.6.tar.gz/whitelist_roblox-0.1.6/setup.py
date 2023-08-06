from setuptools import setup

setup(
    name='whitelist_roblox',
    version='0.1.6',    
    description='Whitelist For Roblox Script',
    author='MaGiXx#6964',
    packages=[
        'wl_magixx', 
        'wl_magixx/discordbot'
    ],
    install_requires=[
        'requests',        
        'disnake'             
    ]
)