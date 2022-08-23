import discord
from discord.ext import commands

from to import *

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents.all())


@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command(aliases=['hi', 'ㅁ'])
async def welcome(ctx):
    await ctx.send('{}님 안녕하세요.'.format(ctx.author.mention))


@bot.command(aliases=['로아정보'])
async def lostArk(ctx):
    sites = ['https://lostark.inven.co.kr/', 'https://loawa.com/', 'https://loa.icepeng.com/']
    result = '인벤: {}\n로아와: {}\n아이스펭: {}\n'.format(sites[0], sites[1], sites[2])
    await ctx.send(result)


@bot.command()
async def FollowUserChat(ctx, *, text):
    await ctx.send(text)


@bot.command(name='관리자')
async def adminCheck(ctx):
    if ctx.guild:
        if ctx.message.author.guild_permissions.administrator:
            await ctx.send('{}님은 관리자입니다.'.format(ctx.author.mention))
        else:
            await ctx.send('{}님은 멤버입니다.}'.format(ctx.author.mention))


@bot.command(name='공지')
async def Announcement(ctx, *, notice):
    admin = ctx.message.author.guild_permissions.administrator
    # channel = ctx.guild.get_channel(1011555379433455646)  # bot_test_area (테스트 시 사용)
    channel = ctx.guild.get_channel(Notice)  # 공지사항 채널
    # Discord 에서 개발자 모드를 켜서 채널의 ID를 가져와 넣는다.
    if admin is True:
        embed = discord.Embed(title="**공지사항**",
                              description="공지사항은 항상 잘 숙지 해주시기 바랍니다.\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(
                                  notice),
                              color=0x2EFEF7)
        embed.set_footer(text="Bot made by. 녹맹이#0997 | 담당 관리자: {}".format(ctx.author))
        await channel.send("@everyone", embed=embed)
        await ctx.send(
            "```**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}```".format(
                channel, ctx.author, notice))

    if admin is False:
        await ctx.send("{}, 당신은 관리자가 아닙니다".format(ctx.author.mention))


# async def on_message(self, message):
#     print('Message from {0.author}: {0.content}'.format(message))


bot.run(Token)
