import discord
from discord.ext import commands
import random
import requests
import json
import os
intents = discord.Intents.default()
intents = discord.Intents.default()
intents.members = True
from discord.ui import Button, View
bot = commands.Bot(command_prefix="!", intents=intents)
import random
from dotenv import load_dotenv
load_dotenv()
import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
import discord
import sqlite3
import discord
from discord.ext import commands
import random
import asyncio
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
client_ai = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Se sincronizaron {len(synced)} comandos.")
    except Exception as e:
        print(e)

    print(f"Conectado como {bot.user}")

@bot.tree.command(
    name="everbox",
    description="Información sobre Everbox Studio"
)
async def everbox(interaction: discord.Interaction):
    await interaction.response.send_message(
        "¡Bienvenido a Everbox Studio!\n\n"
        "Ofrecemos soluciones profesionales para comunidades y servidores."
    )

@bot.tree.command(
    name="servicios",
    description="Muestra los servicios de Everbox Studio"
)
async def servicios(interaction: discord.Interaction):
    await interaction.response.send_message(
        "**Servicios de Everbox Studio**\n\n"
        "• Desarrollo de bots personalizados\n"
        "• Diseño gráfico profesional\n"
        "• Creación de páginas web\n"
        "• Videos publicitarios\n"
        "• Banners y material publicitario\n"
        "• Soporte técnico especializado"
    )

@bot.tree.command(
    name="apertura",
    description="Crear una encuesta de apertura"
)
async def apertura(
    interaction: discord.Interaction,
    votos: int,
    staff: str,
    mensaje: str
):

    embed = discord.Embed(
        title="🗳️ | Encuesta Abierta",
        description=(
            "Se ha iniciado una encuesta para realizar una nueva apertura del servidor de roleplay.\n\n"
            f"📌 | **Votos Requeridos:** {votos}\n"
            f"📌 | **Staff:** {staff}\n"
            f"📌 | **Mensaje del Moderador:** {mensaje}\n\n"
            "• Recuerda que está totalmente prohibido ingresar al servidor mientras permanezca cerrado.\n"
            "• Evita jugar o abusar del sistema de votos, esto podría generar sanciones administrativas.\n"
            "• Una vez alcanzada la meta de votos, el equipo revisará la actividad para proceder con la apertura.\n"
            "• Mantente atento a los anuncios oficiales para conocer el horario exacto de apertura.\n\n"
            "⏳ | La encuesta permanecerá activa por tiempo limitado.\n\n"
            "¡Gracias por la paciencia y apoyo a la comunidad! 🎭"
        ),
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.set_author(name="🌴 | Encuesta para Abrir Server!")

    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1517939946219114657/1518632433380229260/Everbox_Studio_Banner.png?ex=6a3aa02a&is=6a394eaa&hm=ea89e3869a4c18f73aeec2b27de62fae1d492dbbf0e4254b1f19b3888d718944&"
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)

@bot.tree.command(
    name="abierto",
    description="Anuncia la apertura del servidor"
)
async def abierto(
    interaction: discord.Interaction,
    staff: discord.Member,
    tiempo: str,
    everyone: bool
):

    embed = discord.Embed(
        title="🌴 | Servidor Abierto",
        description=(
            "La jornada de roleplay ha comenzado y el servidor ya se encuentra abierto para todos los usuarios.\n\n"
            "Gracias por esperar pacientemente la apertura. Ya puedes ingresar y disfrutar de una nueva sesión de rol junto a la comunidad.\n\n"
            "Recuerda respetar la normativa del servidor y mantener un comportamiento adecuado para garantizar una experiencia agradable para todos los jugadores.\n\n"
            f"📌 | **Staff Responsable:** {staff.mention}\n"
            f"📌 | **Tiempo Máximo para unirse:** {tiempo}\n\n"
            "📌 **Antes de ingresar:**\n"
            "• Lee y respeta las reglas del servidor.\n"
            "• Recuerda unirte a los escenarios correspondientes para mejorar la experiencia de rol.\n"
            "• Evita cualquier tipo de antirol o comportamiento tóxico.\n"
            "• Participa de manera responsable para evitar sanciones innecesarias.\n\n"
            "🔓 El acceso al servidor ha sido habilitado nuevamente.\n\n"
            "¡Les deseamos una excelente sesión de rol! 🎭"
        ),
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.set_image(
        url="https://media.discordapp.net/attachments/1517939946219114657/1518632433380229260/Everbox_Studio_Banner.png?ex=6a3aa02a&is=6a394eaa&hm=ea89e3869a4c18f73aeec2b27de62fae1d492dbbf0e4254b1f19b3888d718944&=&format=webp&quality=lossless&width=982&height=552"
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    mensaje = "@everyone" if everyone else ""

    await interaction.response.send_message(
        content=mensaje,
        embed=embed
    )
@bot.tree.command(
    name="dni",
    description="Genera un DNI de Roleplay"
)
async def dni(
    interaction: discord.Interaction,
    nombres: str,
    apellido: str,
    usuario_roblox: str,
    fecha_nacimiento: str,
    nacionalidad: str,
    edad: int,
    tipo_sangre: str
):

    # Generar RUT aleatorio
    numero = random.randint(10000000, 25000000)
    dv = random.choice(["0","1","2","3","4","5","6","7","8","9","K"])
    rut = f"{numero}-{dv}"

    embed = discord.Embed(
        title="🪪 | Documento Nacional de Identidad",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="📛 Nombres",
        value=nombres,
        inline=True
    )

    embed.add_field(
        name="📛 Apellido",
        value=apellido,
        inline=True
    )

    embed.add_field(
        name="🎮 Usuario de Roblox",
        value=usuario_roblox,
        inline=False
    )

    embed.add_field(
        name="📅 Fecha de Nacimiento",
        value=fecha_nacimiento,
        inline=True
    )

    embed.add_field(
        name="🌎 Nacionalidad",
        value=nacionalidad,
        inline=True
    )

    embed.add_field(
        name="🎂 Edad",
        value=f"{edad} años",
        inline=True
    )

    embed.add_field(
        name="🩸 Tipo de Sangre",
        value=tipo_sangre,
        inline=True
    )

    embed.add_field(
        name="🆔 RUT",
        value=rut,
        inline=True
    )

    # Obtener avatar de Roblox
    try:
        respuesta = requests.post(
            "https://users.roblox.com/v1/usernames/users",
            json={
                "usernames": [usuario_roblox],
                "excludeBannedUsers": True
            }
        )

        datos = respuesta.json()

        if datos["data"]:
            user_id = datos["data"][0]["id"]

            avatar = requests.get(
                f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=420x420&format=Png&isCircular=false"
            )

            avatar_data = avatar.json()
            avatar_url = avatar_data["data"][0]["imageUrl"]

            embed.set_thumbnail(url=avatar_url)

    except:
        pass

    # Guardar DNI
    dnis = {}

    if os.path.exists("dnis.json"):
        with open("dnis.json", "r", encoding="utf-8") as f:
            dnis = json.load(f)

    dnis[usuario_roblox.lower()] = {
        "nombres": nombres,
        "apellido": apellido,
        "usuario_roblox": usuario_roblox,
        "fecha_nacimiento": fecha_nacimiento,
        "nacionalidad": nacionalidad,
        "edad": edad,
        "tipo_sangre": tipo_sangre,
        "rut": rut
    }

    with open("dnis.json", "w", encoding="utf-8") as f:
        json.dump(dnis, f, indent=4, ensure_ascii=False)

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)
@bot.tree.command(
    name="verdni",
    description="Ver el DNI de un usuario"
)
async def verdni(
    interaction: discord.Interaction,
    usuario_roblox: str
):

    if not os.path.exists("dnis.json"):
        await interaction.response.send_message(
            "❌ No hay DNIs registrados.",
            ephemeral=True
        )
        return

    with open("dnis.json", "r", encoding="utf-8") as f:
        dnis = json.load(f)

    usuario = usuario_roblox.lower()

    if usuario not in dnis:
        await interaction.response.send_message(
            "❌ No se encontró un DNI para este usuario.",
            ephemeral=True
        )
        return

    datos = dnis[usuario]

    embed = discord.Embed(
        title="🪪 | Documento Nacional de Identidad",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="📛 Nombres",
        value=datos["nombres"],
        inline=True
    )

    embed.add_field(
        name="📛 Apellido",
        value=datos["apellido"],
        inline=True
    )

    embed.add_field(
        name="🎮 Usuario de Roblox",
        value=datos["usuario_roblox"],
        inline=False
    )

    embed.add_field(
        name="📅 Fecha de Nacimiento",
        value=datos["fecha_nacimiento"],
        inline=True
    )

    embed.add_field(
        name="🌎 Nacionalidad",
        value=datos["nacionalidad"],
        inline=True
    )

    embed.add_field(
        name="🎂 Edad",
        value=f'{datos["edad"]} años',
        inline=True
    )

    embed.add_field(
        name="🩸 Tipo de Sangre",
        value=datos["tipo_sangre"],
        inline=True
    )

    embed.add_field(
        name="🆔 RUT",
        value=datos["rut"],
        inline=True
    )

    # Obtener avatar de Roblox
    try:
        respuesta = requests.post(
            "https://users.roblox.com/v1/usernames/users",
            json={
                "usernames": [datos["usuario_roblox"]],
                "excludeBannedUsers": True
            }
        )

        roblox_data = respuesta.json()

        if roblox_data["data"]:
            user_id = roblox_data["data"][0]["id"]

            avatar = requests.get(
                f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=420x420&format=Png&isCircular=false"
            )

            avatar_data = avatar.json()
            avatar_url = avatar_data["data"][0]["imageUrl"]

            embed.set_thumbnail(url=avatar_url)

    except:
        pass

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)


    await interaction.response.send_message(embed=embed)

@bot.tree.command(
    name="registrarmulta",
    description="Registra una multa a un ciudadano"
)
async def registrarmulta(
    interaction: discord.Interaction,
    usuario_roblox: str,
    motivo: str,
    monto: int,
    funcionario: discord.Member
):

    multas = {}

    if os.path.exists("multas.json"):
        with open("multas.json", "r", encoding="utf-8") as f:
            multas = json.load(f)

    usuario = usuario_roblox.lower()

    if usuario not in multas:
        multas[usuario] = []

    multas[usuario].append({
        "motivo": motivo,
        "monto": monto,
        "funcionario": funcionario.display_name
    })

    with open("multas.json", "w", encoding="utf-8") as f:
        json.dump(multas, f, indent=4, ensure_ascii=False)

    embed = discord.Embed(
        title="🚔 | Multa Registrada",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="🎮 Usuario de Roblox",
        value=usuario_roblox,
        inline=False
    )

    embed.add_field(
        name="📄 Motivo",
        value=motivo,
        inline=False
    )

    embed.add_field(
        name="💰 Monto",
        value=f"${monto:,}",
        inline=True
    )

    embed.add_field(
        name="👮 Funcionario Responsable",
        value=funcionario.mention,
        inline=True
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)
@bot.tree.command(
    name="vermultas",
    description="Ver las multas de un ciudadano"
)
async def vermultas(
    interaction: discord.Interaction,
    usuario_roblox: str
):

    if not os.path.exists("multas.json"):
        await interaction.response.send_message(
            "❌ No hay multas registradas.",
            ephemeral=True
        )
        return

    with open("multas.json", "r", encoding="utf-8") as f:
        multas = json.load(f)

    usuario = usuario_roblox.lower()

    if usuario not in multas:
        await interaction.response.send_message(
            "❌ Este usuario no posee multas registradas.",
            ephemeral=True
        )
        return

    embed = discord.Embed(
        title="🚔 | Historial de Multas",
        description=f"**Ciudadano:** {usuario_roblox}",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    for i, multa in enumerate(multas[usuario], start=1):
        embed.add_field(
            name=f"📄 Multa #{i}",
            value=(
                f"**Motivo:** {multa['motivo']}\n"
                f"**Monto:** ${multa['monto']:,}\n"
                f"**Funcionario:** {multa['funcionario']}"
            ),
            inline=False
        )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)
@bot.tree.command(
    name="registrardelito",
    description="Registra un delito a un ciudadano"
)
async def registrardelito(
    interaction: discord.Interaction,
    usuario_roblox: str,
    delito: str,
    condena: str,
    funcionario: discord.Member
):

    delitos = {}

    if os.path.exists("delitos.json"):
        with open("delitos.json", "r", encoding="utf-8") as f:
            delitos = json.load(f)

    usuario = usuario_roblox.lower()

    if usuario not in delitos:
        delitos[usuario] = []

    delitos[usuario].append({
        "delito": delito,
        "condena": condena,
        "funcionario": funcionario.display_name
    })

    with open("delitos.json", "w", encoding="utf-8") as f:
        json.dump(delitos, f, indent=4, ensure_ascii=False)

    embed = discord.Embed(
        title="⚖️ | Delito Registrado",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="🎮 Ciudadano",
        value=usuario_roblox,
        inline=False
    )

    embed.add_field(
        name="📄 Delito",
        value=delito,
        inline=False
    )

    embed.add_field(
        name="⛓️ Condena",
        value=condena,
        inline=True
    )

    embed.add_field(
        name="👮 Funcionario Responsable",
        value=funcionario.mention,
        inline=True
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)

@bot.tree.command(
    name="verdelitos",
    description="Ver el historial delictivo de un ciudadano"
)
async def verdelitos(
    interaction: discord.Interaction,
    usuario_roblox: str
):

    if not os.path.exists("delitos.json"):
        await interaction.response.send_message(
            "❌ No hay delitos registrados.",
            ephemeral=True
        )
        return

    with open("delitos.json", "r", encoding="utf-8") as f:
        delitos = json.load(f)

    usuario = usuario_roblox.lower()

    if usuario not in delitos:
        await interaction.response.send_message(
            "❌ Este ciudadano no posee delitos registrados.",
            ephemeral=True
        )
        return

    embed = discord.Embed(
        title="⚖️ | Historial Delictivo",
        description=f"**Ciudadano:** {usuario_roblox}",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    for i, delito in enumerate(delitos[usuario], start=1):
        embed.add_field(
            name=f"📄 Delito #{i}",
            value=(
                f"**Delito:** {delito['delito']}\n"
                f"**Condena:** {delito['condena']}\n"
                f"**Funcionario:** {delito['funcionario']}"
            ),
            inline=False
        )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)

@bot.tree.command(
    name="cerrado",
    description="Anuncia el cierre del servidor"
)
async def cerrado(
    interaction: discord.Interaction,
    funcionario: discord.Member,
    everyone: bool
):

    embed = discord.Embed(
        title="🌴 | Servidor Cerrado",
        description=(
            "Se ha finalizado la jornada de roleplay y el servidor ha sido cerrado temporalmente.\n\n"
            "Gracias a todos los que participaron en esta sesión. Esperamos que hayan disfrutado la experiencia y hayan contribuido a un buen ambiente dentro del rol.\n\n"
            "Recuerda siempre respetar la normativa y mantener un buen comportamiento para evitar sanciones en futuras aperturas.\n\n"
            "Mantente atento a los próximos anuncios para la siguiente apertura del servidor.\n\n"
            f"👮 | **Funcionario Responsable:** {funcionario.mention}\n\n"
            "🔒 El acceso se encuentra deshabilitado por el momento.\n\n"
            "¡Nos vemos en la próxima sesión de rol! 🎭"
        ),
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.set_image(
        url="https://media.discordapp.net/attachments/1517939946219114657/1518632433380229260/Everbox_Studio_Banner.png?ex=6a3aa02a&is=6a394eaa&hm=ea89e3869a4c18f73aeec2b27de62fae1d492dbbf0e4254b1f19b3888d718944&=&format=webp&quality=lossless&width=982&height=552"
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    mensaje = "@everyone" if everyone else ""

    await interaction.response.send_message(
        content=mensaje,
        embed=embed
    )

from discord import app_commands

@bot.tree.command(
    name="registrarcompra",
    description="Registra una compra realizada en Everbox Studio"
)
@app_commands.choices(servicio=[
    app_commands.Choice(name="Video", value="Video"),
    app_commands.Choice(name="Liverys", value="Liverys"),
    app_commands.Choice(name="Webs", value="Webs"),
    app_commands.Choice(name="Foto", value="Foto"),
    app_commands.Choice(name="Bot", value="Bot"),
    app_commands.Choice(name="Server", value="Server"),
    app_commands.Choice(name="Banner", value="Banner")
])
async def registrarcompra(
    interaction: discord.Interaction,
    cliente: discord.Member,
    servicio: app_commands.Choice[str],
    precio: int,
    funcionario: discord.Member,
    informacion: str = "Sin información adicional"
):

    compras = {}

    if os.path.exists("compras.json"):
        with open("compras.json", "r", encoding="utf-8") as f:
            compras = json.load(f)

    cliente_id = str(cliente.id)

    if cliente_id not in compras:
        compras[cliente_id] = []

    compras[cliente_id].append({
        "servicio": servicio.value,
        "precio": precio,
        "funcionario": funcionario.display_name,
        "informacion": informacion
    })

    with open("compras.json", "w", encoding="utf-8") as f:
        json.dump(compras, f, indent=4, ensure_ascii=False)

    embed = discord.Embed(
        title="🛒 | Compra Registrada",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="👤 Cliente",
        value=cliente.mention,
        inline=False
    )

    embed.add_field(
        name="🛍️ Servicio Adquirido",
        value=servicio.value,
        inline=True
    )

    embed.add_field(
        name="💰 Precio",
        value=f"${precio:,}",
        inline=True
    )

    embed.add_field(
        name="👨‍💼 Funcionario Responsable",
        value=funcionario.mention,
        inline=False
    )

    embed.add_field(
        name="📝 Información Adicional",
        value=informacion,
        inline=False
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name="avisarrol",
    description="Envía un mensaje privado a todos los usuarios con un rol específico"
)
async def avisarrol(
    interaction: discord.Interaction,
    rol: discord.Role,
    mensaje: str
):

    await interaction.response.defer(ephemeral=True)

    enviados = 0
    errores = 0

    for miembro in rol.members:
        try:
            await miembro.send(
                f"📩 **Mensaje de Everbox Studio**\n\n{mensaje}"
            )
            enviados += 1
        except:
            errores += 1

    embed = discord.Embed(
        title="📨 | Mensajes Enviados",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="🎭 Rol",
        value=rol.mention,
        inline=False
    )

    embed.add_field(
        name="✅ Mensajes enviados",
        value=str(enviados),
        inline=True
    )

    embed.add_field(
        name="❌ Errores",
        value=str(errores),
        inline=True
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.followup.send(
        embed=embed,
        ephemeral=True
    )
# ================= SISTEMA DE TICKETS EVERBOX =================

class TicketPanel(View):
    def __init__(self):
        super().__init__(timeout=None)

    async def crear_ticket(self, interaction: discord.Interaction, tipo: str):

        guild = interaction.guild

        categoria = discord.utils.get(
            guild.categories,
            name="TICKETS"
        )

        if categoria is None:
            await interaction.response.send_message(
                "❌ No se encontró la categoría **TICKETS**.",
                ephemeral=True
            )
            return

        nombre_canal = f"{tipo}-{interaction.user.name}".lower()
        nombre_canal = nombre_canal.replace(" ", "-")

        # Verificar si ya tiene un ticket
        for canal in categoria.text_channels:
            if canal.name == nombre_canal:
                await interaction.response.send_message(
                    f"❌ Ya tienes un ticket abierto: {canal.mention}",
                    ephemeral=True
                )
                return

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                view_channel=False
            ),

            interaction.user: discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                read_message_history=True
            )
        }

        canal = await guild.create_text_channel(
            name=nombre_canal,
            category=categoria,
            overwrites=overwrites
        )

        embed = discord.Embed(
            title="🎫 | Ticket Creado",
            description=(
                f"Bienvenido {interaction.user.mention}\n\n"
                f"Has abierto un ticket de **{tipo.replace('-', ' ').title()}**.\n\n"
                "Un miembro del staff te atenderá lo antes posible.\n\n"
                "📝 Explica detalladamente tu consulta."
            ),
            color=discord.Color.from_rgb(255, 255, 255)
        )

        embed.set_footer(
            text="Everbox Studio © Todos los derechos reservados"
        )

        await canal.send(embed=embed)

        await interaction.response.send_message(
            f"✅ Ticket creado correctamente: {canal.mention}",
            ephemeral=True
        )

    @discord.ui.button(
        label="Soporte General",
        emoji="⭐",
        style=discord.ButtonStyle.primary
    )
    async def soporte(self, interaction, button):
        await self.crear_ticket(interaction, "soporte-general")

    @discord.ui.button(
        label="Solicitar Fundación",
        emoji="🏛️",
        style=discord.ButtonStyle.success
    )
    async def fundacion(self, interaction, button):
        await self.crear_ticket(interaction, "fundacion")

    @discord.ui.button(
        label="Reportes Everbox",
        emoji="🚨",
        style=discord.ButtonStyle.danger
    )
    async def reportes(self, interaction, button):
        await self.crear_ticket(interaction, "reportes")

    @discord.ui.button(
        label="Alianzas Everbox",
        emoji="🤝",
        style=discord.ButtonStyle.secondary
    )
    async def alianzas(self, interaction, button):
        await self.crear_ticket(interaction, "alianzas")

    @discord.ui.button(
        label="Compras",
        emoji="🛒",
        style=discord.ButtonStyle.success
    )
    async def compras(self, interaction, button):
        await self.crear_ticket(interaction, "compras")


@bot.tree.command(
    name="paneltickets",
    description="Envía el panel de tickets"
)
async def paneltickets(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🎫 | Sistema de Soporte - Everbox Studio",
        description=(
            "Bienvenido al sistema oficial de soporte de **Everbox Studio**.\n\n"

            "⭐ **Soporte General**\n"
            "Resuelve dudas generales relacionadas con la comunidad.\n\n"

            "🏛️ **Solicitar Fundación**\n"
            "Permite solicitar comunicación con Fundación.\n\n"

            "🚨 **Reportes Everbox**\n"
            "Reporta usuarios, servidores o miembros del staff.\n\n"

            "🤝 **Alianzas Everbox**\n"
            "Solicita alianzas o afiliaciones.\n\n"

            "🛒 **Compras**\n"
            "Resuelve dudas sobre servicios y compras.\n\n"

            "⚠️ El mal uso del sistema puede derivar en sanciones.\n\n"

            "📌 Presiona un botón para abrir un ticket."
        ),
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(
        embed=embed,
        view=TicketPanel()
    )



@bot.tree.command(
    name="registrarvehiculo",
    description="Registra un vehículo"
)
async def registrarvehiculo(
    interaction: discord.Interaction,
    propietario: str,
    marca: str,
    modelo: str,
    color: str
):

    matricula = (
        ''.join(random.choices(string.ascii_uppercase, k=3))
        + "-"
        + ''.join(random.choices(string.digits, k=3))
    )

    embed = discord.Embed(
        title="🚗 | Registro de Vehículo",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="👤 Propietario",
        value=propietario,
        inline=True
    )

    embed.add_field(
        name="🏭 Marca",
        value=marca,
        inline=True
    )

    embed.add_field(
        name="🚘 Modelo",
        value=modelo,
        inline=True
    )

    embed.add_field(
        name="🎨 Color",
        value=color,
        inline=True
    )

    embed.add_field(
        name="🔖 Matrícula",
        value=matricula,
        inline=True
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)

@bot.tree.command(
    name="registrararma",
    description="Registra un arma"
)
async def registrararma(
    interaction: discord.Interaction,
    propietario: str,
    tipo_arma: str,
    calibre: str
):

    serie = ''.join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=10
        )
    )

    embed = discord.Embed(
        title="🔫 | Registro de Arma",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="👤 Propietario",
        value=propietario,
        inline=True
    )

    embed.add_field(
        name="🔫 Tipo de Arma",
        value=tipo_arma,
        inline=True
    )

    embed.add_field(
        name="📏 Calibre",
        value=calibre,
        inline=True
    )

    embed.add_field(
        name="🆔 Número de Serie",
        value=serie,
        inline=False
    )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)
@bot.tree.command(
    name="vervehiculos",
    description="Ver los vehículos registrados de un usuario"
)
async def vervehiculos(
    interaction: discord.Interaction,
    usuario_roblox: str
):

    if usuario_roblox not in vehiculos:
        await interaction.response.send_message(
            "❌ Este usuario no tiene vehículos registrados."
        )
        return

    embed = discord.Embed(
        title=f"🚗 | Vehículos de {usuario_roblox}",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    for vehiculo in vehiculos[usuario_roblox]:
        embed.add_field(
            name=f"🚘 {vehiculo['marca']} {vehiculo['modelo']}",
            value=(
                f"🎨 Color: {vehiculo['color']}\n"
                f"🔖 Matrícula: {vehiculo['matricula']}"
            ),
            inline=False
        )

    embed.set_footer(
        text="Everbox Studio© Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)
@bot.tree.command(
    name="verarmas",
    description="Ver las armas registradas de un usuario"
)
async def verarmas(
    interaction: discord.Interaction,
    usuario_roblox: str
):

    if usuario_roblox not in armas:
        await interaction.response.send_message(
            "❌ Este usuario no tiene armas registradas."
        )
        return

    embed = discord.Embed(
        title=f"🔫 | Armas de {usuario_roblox}",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    for arma in armas[usuario_roblox]:
        embed.add_field(
            name=f"🔫 {arma['tipo']}",
            value=(
                f"📏 Calibre: {arma['calibre']}\n"
                f"🆔 Serie: {arma['serie']}"
            ),
            inline=False
        )

    embed.set_footer(
        text="Everbox Studio © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)

@bot.tree.command(
    name="calificarstaff",
    description="Califica a un funcionario"
)
async def calificarstaff(
    interaction: discord.Interaction,
    funcionario: str,
    calificacion: int
):

    if calificacion < 1 or calificacion > 5:
        await interaction.response.send_message(
            "❌ La calificación debe ser entre 1 y 5."
        )
        return

    if funcionario not in staff_calificaciones:
        staff_calificaciones[funcionario] = []

    staff_calificaciones[funcionario].append(calificacion)

    promedio = (
        sum(staff_calificaciones[funcionario])
        / len(staff_calificaciones[funcionario])
    )

    embed = discord.Embed(
        title="⭐ | Funcionario Calificado",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="👮 Funcionario",
        value=funcionario,
        inline=True
    )

    embed.add_field(
        name="⭐ Calificación",
        value=f"{calificacion}/5",
        inline=True
    )

    embed.add_field(
        name="📊 Promedio Actual",
        value=f"{promedio:.1f}/5",
        inline=True
    )

    embed.set_footer(
        text="Elite Chile Roleplay © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)
@bot.tree.command(
    name="topstaff",
    description="Muestra el ranking de los mejores staff"
)
async def topstaff(interaction: discord.Interaction):

    if not staff_calificaciones:
        await interaction.response.send_message(
            "❌ No hay calificaciones registradas."
        )
        return

    ranking = []

    for staff, notas in staff_calificaciones.items():
        promedio = sum(notas) / len(notas)
        ranking.append((staff, promedio, len(notas)))

    ranking.sort(key=lambda x: x[1], reverse=True)

    embed = discord.Embed(
        title="🏆 | Top Staff - Elite Chile Roleplay",
        description="Ranking oficial de los funcionarios mejor calificados.",
        color=discord.Color.from_rgb(255, 255, 255)
    )

    posiciones = ["🥇", "🥈", "🥉"]

    for i, (staff, promedio, total) in enumerate(ranking[:10]):

        emoji = posiciones[i] if i < 3 else f"#{i+1}"

        embed.add_field(
            name=f"{emoji} {staff}",
            value=(
                f"⭐ Promedio: **{promedio:.1f}/5**\n"
                f"📝 Calificaciones recibidas: **{total}**"
            ),
            inline=False
        )

    embed.set_footer(
        text="Elite Chile Roleplay © Todos los derechos reservados"
    )

    await interaction.response.send_message(embed=embed)
@bot.tree.command(
    name="firmar",
    description="Genera un documento para firmar"
)
async def firmar(
    interaction: discord.Interaction,
    tipo: str,
    usuario: discord.Member
):

    tipos_validos = [
        "Movimiento de dinero",
        "Trabajo nuevo",
        "Documento"
    ]

    if tipo not in tipos_validos:
        await interaction.response.send_message(
            "❌ Tipos válidos:\n"
            "• Movimiento de dinero\n"
            "• Trabajo nuevo\n"
            "• Documento",
            ephemeral=True
        )
        return

    embed = discord.Embed(
        title="🖋️ | Documento de Firma",
        description=(
            f"Se ha generado un documento de tipo **{tipo}**.\n\n"
            f"🤝 **Solicitante:** {interaction.user.mention}\n"
            f"👤 **Interactuando con:** {usuario.mention}\n\n"
            "Ambas partes deberán confirmar y aceptar este documento.\n\n"
            "Al aceptar, ambas partes reconocen haber leído y aceptado los términos del acuerdo."
        ),
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.add_field(
        name="🖊️ Firma del Solicitante",
        value=f"**{interaction.user.display_name}**",
        inline=True
    )

    embed.add_field(
        name="🖊️ Firma del Receptor",
        value=f"**{usuario.display_name}**",
        inline=True
    )
    embed.set_footer(
        text="Elite Chile Roleplay © Todos los derechos reservados"
)
async def preguntar_ia(pregunta: str):
    try:
        respuesta = client_ai.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
Eres el asistente oficial de Chile Metropolitano Roleplay.

Reglas:
- Responde siempre en español
- Sé claro, breve y útil
- No inventes información del servidor

Usuario pregunta:
{pregunta}
"""
        )

        return respuesta.text

    except Exception as e:
        print(e)
        return f"❌ Error con Gemini: {e}"
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user in message.mentions:

        pregunta = (
            message.content
            .replace(f"<@{bot.user.id}>", "")
            .replace(f"<@!{bot.user.id}>", "")
            .strip()
        )

        if not pregunta:
            await message.reply("¿En qué puedo ayudarte?")
            return

        async with message.channel.typing():
            respuesta = await preguntar_ia(pregunta)

        await message.reply(respuesta)

    await bot.process_commands(message)
conn = sqlite3.connect("economia.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    user_id INTEGER PRIMARY KEY,
    dinero INTEGER DEFAULT 0,
    banco INTEGER DEFAULT 0
)
""")

def asegurar_usuario(user_id):
    cursor.execute("SELECT * FROM usuarios WHERE user_id = ?", (user_id,))
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO usuarios (user_id, dinero, banco) VALUES (?, 0, 0)",
            (user_id,)
        )
        conn.commit()


def get_dinero(user_id):
    asegurar_usuario(user_id)
    cursor.execute("SELECT dinero, banco FROM usuarios WHERE user_id = ?", (user_id,))
    return cursor.fetchone()


def update_dinero(user_id, cantidad):
    asegurar_usuario(user_id)
    cursor.execute("UPDATE usuarios SET dinero = dinero + ? WHERE user_id = ?", (cantidad, user_id))
    conn.commit()

@bot.command()
async def balance(ctx):
    dinero, banco = get_dinero(ctx.author.id)

    embed = discord.Embed(
        title="💰 Balance",
        description=f"Dinero: ${dinero}\nBanco: ${banco}",
        color=discord.Color.green()
    )

    await ctx.send(embed=embed)
@bot.command()
async def trabajar(ctx):
    ganar = random.randint(50, 200)
    update_dinero(ctx.author.id, ganar)

    await ctx.send(f"💼 Trabajaste y ganaste ${ganar}")
@bot.command()
async def daily(ctx):
    ganar = random.randint(200, 500)
    update_dinero(ctx.author.id, ganar)

    await ctx.send(f"🎁 Recompensa diaria: ${ganar}")

contexto_economia = """
Sistema del servidor:
- Moneda: $
- Puedes trabajar, robar, reclamar daily
- Economía RP de Chile Metropolitano Roleplay
"""

prompt = f"""
{contexto_economia}

Usuario pregunta:
{pregunta}
"""
if "como gano dinero" in message.content.lower():
    await message.reply("💡 Puedes usar !trabajar, !daily o intentar !robar en el servidor.")
    return
@bot.command()
async def apostar(ctx, partido: str, equipo: str, monto: int):
    dinero, banco = get_dinero(ctx.author.id)

    if monto <= 0:
        return await ctx.send("❌ El monto debe ser mayor a 0")

    if dinero < monto:
        return await ctx.send("❌ No tienes suficiente dinero")

    # descontar dinero
    update_dinero(ctx.author.id, -monto)

    cursor.execute(
        "INSERT INTO apuestas VALUES (?, ?, ?, ?)",
        (ctx.author.id, partido, equipo.lower(), monto)
    )
    conn.commit()

    await ctx.send(
        f"⚽ Apuesta registrada!\n"
        f"Partido: {partido}\n"
        f"Equipo: {equipo}\n"
        f"Monto: ${monto}"
    )

@bot.command()
@commands.has_permissions(administrator=True)
async def resultado(ctx, partido: str, ganador: str):
    ganador = ganador.lower()

    cursor.execute(
        "SELECT user_id, monto FROM apuestas WHERE partido = ? AND equipo = ?",
        (partido, ganador)
    )

    ganadores = cursor.fetchall()

    if not ganadores:
        return await ctx.send("❌ Nadie acertó el resultado")

    total_pagado = 0

    for user_id, monto in ganadores:
        premio = monto * 2  # x2 ganancia
        update_dinero(user_id, premio)
        total_pagado += premio

    cursor.execute("DELETE FROM apuestas WHERE partido = ?", (partido,))
    conn.commit()

    await ctx.send(
        f"🏆 Resultado del partido {partido}: {ganador.upper()}\n"
        f"💰 Se pagaron ${total_pagado} en premios"
    )

@bot.command()
async def misapuestas(ctx):
    cursor.execute(
        "SELECT partido, equipo, monto FROM apuestas WHERE user_id = ?",
        (ctx.author.id,)
    )

    data = cursor.fetchall()

    if not data:
        return await ctx.send("❌ No tienes apuestas activas")

    msg = "⚽ Tus apuestas:\n"
    for partido, equipo, monto in data:
        msg += f"- {partido}: {equipo} (${monto})\n"

    await ctx.send(msg)

conn.commit()

load_dotenv()

client_ai = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

import os

bot.run(os.getenv("TOKEN"))