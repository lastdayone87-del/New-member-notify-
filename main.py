import os
import discord

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not TOKEN or not CHANNEL_ID:
    print("❌ ERROR: Missing TOKEN or CHANNEL_ID in environment variables!")
    exit(1)

CHANNEL_ID = int(CHANNEL_ID)
client = discord.Client()

async def send_notification(content):
    try:
        channel = client.get_channel(CHANNEL_ID) or await client.fetch_channel(CHANNEL_ID)
        if channel:
            await channel.send(content)
        else:
            print(f"❌ Could not find channel with ID: {CHANNEL_ID}")
    except Exception as e:
        print(f"❌ Error sending message to channel: {e}")

@client.event
async def on_ready():
    print(f"✅ Connected as {client.user} ({client.user.id})")

@client.event
async def on_member_join(member):
    msg = f"🔔 **New Member Alert:** `{member.name}` in **{member.guild.name}**"
    await send_notification(msg)

client.run(TOKEN)
