import disnake
import wl_magixx

from disnake.ext import commands

class whitelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    def is_admins(inter: disnake.ApplicationCommandInteraction):
        if inter.author.id in wl_magixx.admins:
            return True

    @commands.slash_command(name="add_whitelist", description="Add user to whitelist")
    @commands.check(is_admins)
    async def add_in_whitelist(self, inter: disnake.ApplicationCommandInteraction, discord_id: str):
        data = wl_magixx.add_whitelist(discord_id=discord_id)
        if data.get("status") == True:
            return await inter.send(f"Successfully added whitelist <@{discord_id}>!")
        return await inter.send("Error", ephemeral=True, delete_after=10)

    @commands.slash_command(name="delete_whitelist", description="Delete user from whitelist")
    @commands.check(is_admins)
    async def del_from_whitelist(self, inter: disnake.ApplicationCommandInteraction, discord_id: str):
        data = wl_magixx.del_whitelist(discord_id=discord_id)
        if data.get("status") == True:
            return await inter.send(f"Successfully deleted whitelist <@{discord_id}>!")
        return await inter.send("Error", ephemeral=True, delete_after=10)

    @commands.slash_command(name="key", description="This command for whitelist user. Get Key Redeem")
    async def get_key_from_whitelist(self, inter: disnake.ApplicationCommandInteraction):
        data = wl_magixx.whitelist(discord_id=inter.author.id)
        if data.get("status") == True:
            return await inter.send(f"`https://1.kelprepl.repl.co/getkey/{wl_magixx.name}?redeem={data.get('key')}`", ephemeral=True)
        return await inter.send("Your no whitelist!", ephemeral=True, delete_after=10)

    @commands.slash_command(name="reset", description="This command for whitelist user. Reset IP and KEY")
    async def reset_whitelist(self, inter: disnake.ApplicationCommandInteraction):
        data = wl_magixx.reset_whitelist(discord_id=inter.author.id)
        if data.get("status") == True:
            return await inter.send(f"Successfully reset use `/key`!")
        return await inter.send("Your no whitelist!", ephemeral=True, delete_after=10)

def setup(bot):
    bot.add_cog(whitelist(bot))