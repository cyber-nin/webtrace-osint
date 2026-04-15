from telethon.tl.functions.messages import ImportChatInviteRequest

async def join_group(client, invite_link):
    try:
        hash = invite_link.split("/")[-1]
        await client(ImportChatInviteRequest(hash))
        print(f"[+] Joined: {invite_link}")
    except Exception as e:
        print(f"[!] Failed: {e}")
