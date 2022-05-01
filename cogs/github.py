import json
from config import github_token
from discord.ext import commands
from github import Github, UnknownObjectException

g = Github(github_token)
repo = g.get_repo("W-OVERFLOW-github/test")


class Github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def files(self, ctx):
        contents = repo.get_contents("")
        msg = ""
        for file in contents:
            msg += file.path + "\n"
        await ctx.reply(msg)

    @commands.command(aliases=["append"])
    async def edit(self, ctx, file, key, value, *, message="Commit via W-OVERFLOW bot"):
        try:
            contents = repo.get_contents(file)
            content = contents.decoded_content.decode("utf-8")
            data = json.loads(content)
            data[key] = value
            content = json.dumps(data, indent=4)
            repo.update_file(contents.path, message, content, contents.sha)
            await ctx.reply("Updated file.")
        except UnknownObjectException:
            await ctx.reply("File not found.")


def setup(bot):
    bot.add_cog(Github(bot))
