# ESInformación: Aplicación Streamlit interactiva
import streamlit as st

# Configuración general
st.set_page_config(page_title="ESInformación 🧠💬", page_icon="🌈", layout="centered")

# Estilos personalizados y fondo cálido
st.markdown("""
    <style>
    body {
        background-color: #fff4f8;
    }

    /* Animaciones en los laterales */
    .animacion-lateral {
        position: fixed;
        top: 10%;
        width: 120px;
        z-index: 0;
        opacity: 0.8;
    }

    .izquierda {
        left: 0;
        animation: flotar 5s ease-in-out infinite alternate;
    }

    .derecha {
        right: 0;
        animation: flotar 4s ease-in-out infinite alternate-reverse;
    }

    @keyframes flotar {
        0% { transform: translateY(0px); }
        100% { transform: translateY(20px); }
    }
    </style>

    <!-- Stickers animados -->
    <img src="https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif" class="animacion-lateral izquierda">
    <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" class="animacion-lateral derecha">
""", unsafe_allow_html=True)

# Título principal
st.markdown('<div class="titulo">🌈 ¡Bienvenidx a <i>ESInformación</i>! 🧠💬</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Un espacio seguro para aprender sobre Educación Sexual Integral (ESI)</div>', unsafe_allow_html=True)

# Presentación
st.write("""
La Educación Sexual Integral busca brindar a los estudiantes información confiable sobre su cuerpo, la sexualidad y la afectividad, para que puedan tomar decisiones libres y responsables.

Promueve el respeto por uno mismo y por los demás, fomenta relaciones sanas y equitativas, y ayuda a prevenir la violencia, los embarazos no deseados y las infecciones de transmisión sexual.

Además, enseña a valorar la diversidad, cuestionar estereotipos de género y fortalecer la autoestima, el autocuidado y la autoafirmación.
""")

# Inputs
nombre = st.text_input("¿Cómo te llamas?")
edad = st.number_input("¿Cuántos años tienes?", min_value=0, step=1)

if nombre and edad:
    if edad < 18:
        st.info(f"¡Perfecto, {nombre}! Como eres menor de edad, usaremos un lenguaje claro y respetuoso 😊.")
    else:
        st.success(f"Gracias por confiar en nosotros, {nombre}. Esta herramienta es útil para todxs 🧡.")

st.markdown("<div class='subtitulo'>¿Qué te gustaría conocer en <i>ESInformación</i>?</div>", unsafe_allow_html=True)

with st.container():
    with st.expander("Haz clic para explorar los temas disponibles. Diviérte con el apartado que hemos ido creando para ti ✨", expanded=True):
        opcion = st.selectbox("", [
            "Selecciona una opción",
            "1. ¿Qué es la ESI?",
            "2. Métodos anticonceptivos",
            "3. Mitos y verdades",
            "4. Autocuidado digital y sexting",
            "5. Relaciones afectivas y vínculos sanos",
            "6. Identidad de género y orientación sexual"
        ], key="temas")

    if opcion == "1. ¿Qué es la ESI?":
        st.header("📌 ¿Qué es la ESI?")
        st.markdown("""
La Educación Sexual Integral (ESI) es un enfoque educativo que busca brindar conocimientos científicos, éticos y afectivos sobre la sexualidad. Está diseñada para que niñas, niños y adolescentes desarrollen habilidades para tomar decisiones informadas, responsables y respetuosas sobre su cuerpo y relaciones.

Entre sus objetivos destacan:
- Prevenir embarazos no deseados y enfermedades de transmisión sexual.
- Fomentar el respeto por la diversidad y los derechos humanos.
- Promover relaciones equitativas y libres de violencia.
- Fortalecer la autoestima, el autocuidado y la autoafirmación.

La ESI no reemplaza lo que se enseña en casa, sino que lo complementa, involucrando también a docentes, familias y comunidades.
        """)

    # === SECCIÓN 2 ===
    elif opcion == "2. Métodos anticonceptivos":
        st.header("📌 Métodos Anticonceptivos")
        st.markdown("Haz clic para conocer más sobre cada método:")

        metodos = {
            "🧴 Condón": {
                "img": "https://images.unsplash.com/photo-1575997803451-f0752869e498?q=80&w=1073&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**Condón**
Es el único método que brinda doble protección, ya que previene tanto un embarazo no planificado como las infecciones de transmisión sexual (ITS), incluyendo el VIH. Se debe colocar antes del acto scual.

EFICACIA: El condón masulino tiene una eficacia de 85% para prevenir embarazos no deseados y 95% para prevenir ITS. El condón femenino tiene una eficacia del 79% en su uso común."""
            },
            "💊 Pastillas anticonceptivas": {
                "img": "https://images.unsplash.com/photo-1576065435202-e0a7979b93e3?q=80&w=1117&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**Pastillas anticonceptivas**
Método hormonal que inhibe la ovulación y espesa el moco cervical, dificultando el paso de los espermatozoides. Las píldoras combinadas de estrógenos y progestágenos deben tomarse diariamente a la misma hora. Uso: Diariamente a la misma hora.

Eficacia: 99,7 % si se usa correctamente. También protege contra el cáncer de ovario y endometrio."""

            },
            "💉 Inyecciones": {
                "img": "https://images.unsplash.com/photo-1609009630912-f16dcf3e03a6?q=80&w=688&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**Inyecciones**
Actúan como deteniendo la ovulación y espesan el moco cervical, además que bloquean el paso de los espermatozoides hacia el útero. Puede hacerlo durante ciertos meses, por ejemplo inyectable mensual, te protege todo un mes, además del trimestre que es por tres meses.

Tiene una eficacia de manera mensual de 99.5% y trimestral de 99.7%"""

            },
            "📍 Implante subdérmico": {
                "img": "https://enfamilia.aeped.es/sites/enfamilia.aeped.es/files/images/articulos/implante2.jpg",
                "desc": """**Implante subdérmico**
Es una pequeña varilla flexible colocada debajo de la piel del brazo, libera progestágeno de manera seguida para prevenir el embarazo. Puede proteger hasta por 3 años 

Su eficacia es de 99.95%. Puede causar alteraciones menstruales, pero no interfiere con el acto sexual."""
            },
            "⚙️ Sistema Intrauterino de Levonorgestrel - SIU-LING": {
                "img": "https://images.unsplash.com/photo-1715111641899-b0118be16660?q=80&w=1108&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**SIU Hormonal**
Es un dispositivo pequeño que se inserta en el utero y liberta hormonas, puede proteger hasta por 5 años y es colocado por un profesional.

Tiene un 99.5% de eficacia."""
            },
            "🧲 Dispositivo intrauterino - DIU de cobre": {
                "img": "https://images.unsplash.com/photo-1576070932889-43995345c9b6?q=80&w=1077&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**DIU de cobre**
Pequeño dispositivo recubierto con cobre, que se coloca en el utero para evitar la fertilización, tiene una protección por 12 años y también es colocado por un profesional

Eficacia de 99.4%. No interfiere con el acto sexual"""
            },
            "🚨 Anticonceptivo Oral de Emergencia - AOE": {
                "img": "https://images.unsplash.com/photo-1576069445378-ddc40a383222?q=80&w=1073&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**AOE (pastilla de emergencia)**
Utilizado solo en situaciones de emergencia, como relaciones sin protección o violencia sexual, puede durar hasta 72 horas despúes del actos sexual.

Tiene hasta un 95% de efectividad, tiene mayor efectividad cuanto antes se use. No sustituye al uso regular de otros métodos."""

            }
        }

        for metodo, info in metodos.items():
            with st.expander(metodo):
                st.image(info["img"], use_column_width=True)
                st.markdown(info["desc"])

    # === SECCIÓN 3 ===
    if opcion == "3. Mitos y verdades":
        st.header("🎮 ¿Mito o Verdad?")
        preguntas = [
            ("La educación sexual en la escuela interfiere con lo que enseñan en casa.", "mito", "La educación sexual integral no interfiere con la educación previa que nuestros padres y madres nos ofrecen, sino que por el contrario, la labor de padres y profesores se complementa para asegurar una formación integral." ),
            ("Hablar de sexualidad hace que los adolescentes tengan más relaciones sexuales a temprana edad.", "mito", "Está demostrado que la ESI retrasa el inicio sexual y mejora la toma de decisiones, además ayuda a crecer en conocimiento y valores para vivir la sexualidad con bienestar."),
            ("Hay adultos quienes no tuvieron previa enseñanza sobre la sexualidad, aprendieron solos y les fue bien.", "mito", "Estas son personas que no tuvieron la oportunidad de recibir información integral en la escuela, ello ha generado diversas dudas que les impide disfrutar su sexualidad plenamente. Por ello es importante hablar sobre la ESI."),
            ("La ESI habla sobre identidad de género u orientación sexual en la escuela, sin determinar la sexualidad de las personas.", "verdad", "Verdad, pues enseña a no discriminar y a valorar la diversidad que hay a nuestro alrededor."),
        ]
        aciertos = 0
        for i, (preg, correcta, exp) in enumerate(preguntas):
            st.markdown(f"**{i+1}. {preg}**")
            rpta = st.radio("¿Qué opinas?", ["", "mito", "verdad"], key=f"rpta_{i}")
            if rpta:
                if rpta == correcta:
                    st.success("✔️ ¡Correcto!")
                    aciertos += 1
                else:
                    st.error("❌ Incorrecto")
                st.info(exp)
                st.markdown("---")
                
        if aciertos == 4:
            st.balloons()
            st.markdown(f"<h2 style='text-align: center; color: green;'>🎉 ¡Excelente, {nombre}! Respondiste todas correctamente. ¡Sigue así! 🎉</h2>", unsafe_allow_html=True)
        elif aciertos == 3:
            st.markdown(f"<h2 style='text-align: center;'>👏 ¡Muy bien, {nombre}! Aciertos: 3 de 4. Vas por buen camino.</h2>", unsafe_allow_html=True)
        elif aciertos == 2:
            st.markdown(f"<h3 style='text-align: center;'>🙂 ¡Tú puedes! Acertaste 2, sigue practicando.</h3>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='text-align: center;'>💪 No te desanimes, {nombre}. ¡Sigue aprendiendo y mejorando!</h3>", unsafe_allow_html=True)


    elif opcion == "4. Autocuidado digital y sexting":
        st.header("📱 Autocuidado Digital y Sexting")

        cards = [
            {
                "titulo": "🔐 ¿Qué es el sexting?",
                "contenido": """
                El sexting es el intercambio de imágenes o videos de contenido sexual mediante mensajes o redes. Puede ser riesgoso, especialmente en menores, y derivar en abuso sexual. No es aceptable si no hay consentimiento. Presionar a alguien a enviar fotos íntimas es ilegal.
                """
            },
            {
                "titulo": "📤 Cómo evitar la difusión de contenido íntimo",
                "contenido": """
                La difusión sin autorización de material íntimo viola el derecho a la privacidad, libertad de expresión y derechos sexuales. Evalúa bien a quién se lo compartes. Si recibes contenido sin consentimiento, elimínalo.
                """
            },
            {
                "titulo": "⚖️ Responsabilidad legal",
                "contenido": """
                Difundir material íntimo puede ser penado con hasta 6 años de prisión. Además, pueden sumarse sanciones económicas.
                """
            },
            {
                "titulo": "📞 ¿Dónde pedir ayuda?",
                "contenido": """
                Puedes denunciar con pruebas en la División de Delitos de Alta Tecnología de la Policía Nacional.
                - Llama gratis al 1818 o al (01) 431-8898
                - Escribe a divindat.depcpi@policia.gob.pe
                """
            },
        ]

        for card in cards:
            if st.button(card["titulo"]):
                st.markdown(f"<div class='card'><h4>{card['titulo']}</h4><p>{card['contenido']}</p></div>", unsafe_allow_html=True)

        st.success("Haz clic en cada botón para explorar la información de forma interactiva ✨")

#sección 5
    elif opcion == "5. Relaciones afectivas y vínculos sanos":
        st.header("💞 Relaciones afectivas y vínculos sanos")
        
        tarjetas = [
            {
                "icono": "❤️‍🔥",
                "titulo": "¿Qué es el deseo sexual?",
                "contenido": "El deseo sexual, también conocido como libido o lujuria, es la primera etapa del amor en pareja. Se caracteriza por una fuerte atracción física y el interés en mantener relaciones sexuales. Esta fase está impulsada por las hormonas sexuales: la testosterona y los estrógenos. Este tipo de amor se manifiesta cuando la relación gira principalmente en torno al deseo sexual, ya sea a través de la actividad física, fantasías sexuales o la tensión que se siente al estar cerca de la otra persona."
            },
            {
                "icono": "💖",
                "titulo": "¿Qué es la atracción romántica?",
                "contenido": "La segunda fase del amor de pareja es la atracción romántica o el enamoramiento, y está dominada por tres sustancias clave: la dopamina, la norepinefrina y la serotonina. La dopamina, producida por el hipotálamo en el cerebro, se libera cuando realizamos actividades placenteras. Durante el enamoramiento, los niveles de dopamina se elevan significativamente, junto con la norepinefrina. Estas dos hormonas generan sensaciones de euforia, entusiasmo, energía, y pueden causar una disminución del apetito y del sueño."
            },
            {
                "icono": "❤️",
                "titulo": "¿Qué es el amor?",
                "contenido": "Si nos preguntas qué es el amor, nosotros lo describimos como un sentimiento profundo y complejo que se experimenta hacia otra persona, uno mismo o algo que nos apasiona. Además, te diríamos que el amor implica una conexión emocional, física y espiritual que nos hace sentir felices, plenos y realizados."
            },
            {
                "icono": "🚩",
                "titulo": "Identificar las relaciones tóxicas",
                "contenido": """
Control y desconfianza y celos:
Si tu pareja necesita saber dónde estás todo el tiempo, se molesta cuando no respondes al instante o te exige atención constante, es posible que el "cuidado" o el "interés" esconda un deseo de control.

Manipulación emocional:
Frases como “si me amaras, lo harías” son formas de chantaje emocional. Cuando se usan los sentimientos para presionar o manejar al otro, hay manipulación.

Comunicación tóxica:
El sarcasmo, la crítica constante o el uso del silencio para castigar son señales claras. También lo es el gaslighting, que busca hacerte dudar de tu propia percepción o memoria.

Ignorar tus propias necesidades:
Cambiar tu comportamiento, vestimenta o incluso tener relaciones sexuales sin ganas solo para evitar conflictos, es una forma de ceder que atenta contra tu bienestar.

Minimizar tus emociones:
Comentarios como “eso no es nada” o “te quejas por gusto” niegan lo que sientes. En una relación sana, se validan las emociones, no se ridiculizan.
"""
            },
            {
                "icono": "❓",
                "titulo": "¿Estoy en una relación tóxica?",
                "contenido": "Haz clic aquí para responder algunas preguntas y descubrirlo."
            }
        ]

        for tarjeta in tarjetas:
            if st.button(f"{tarjeta['icono']} {tarjeta['titulo']}"):
                if tarjeta['titulo'] == "¿Estoy en una relación tóxica?":
                    st.markdown("Lee con atención las siguientes preguntas y reflexiona sobre tu situación:")
    
                    preguntas = [
                        "1. ¿Tu pareja apoya tus metas y proyectos, o los minimiza o ridiculiza?",
                        "2. ¿Sientes que haga lo que hagas, nunca es suficiente? ¿Recibes críticas constantes?",
                        "3. ¿Te has ido alejando de tus amigos y familia desde que estás en esta relación?",
                        "4. ¿Tu pareja se burla de tus gustos o aficiones, o los respeta?",
                        "5. ¿Sientes que recurre al chantaje emocional para salirse con la suya?",
                        "6. ¿Te exige explicaciones sobre dónde estuviste, con quién y qué hiciste?",
                        "7. ¿Toma decisiones importantes sin consultarte, aunque te afecten directamente?"
                    ]
                    for pregunta in preguntas:
                        st.markdown(f"- {pregunta}")
    
                    st.subheader("💡 Reflexión")
                    st.markdown("""
    Si al leer estas preguntas sentiste incomodidad o te identificaste con varias situaciones, es importante que prestes atención a tu relación.
    
    En una relación saludable:
    - Se respeta tu individualidad.
    - Tus emociones son validadas, no ridiculizadas.
    - No se recurre al control ni al chantaje.
    - Puedes crecer, desarrollarte y sentirte segura/o.
    
    Si algo no te hace bien, no estás exagerando. Tu bienestar emocional es lo más importante. 
    Habla con alguien de confianza o con un/a profesional. Mereces una relación basada en el respeto y el amor propio.
    """)
                else:
                    st.markdown(f"**{tarjeta['icono']} {tarjeta['titulo']}**\n\n{tarjeta['contenido']}")
                  


#OPCION 6
    elif opcion == "6. Identidad de género y orientación sexual":
        st.header("🌈 Identidad de género y orientación sexual")
        with st.expander("Explora los conceptos clave", expanded=True):
            st.write("Conoce los conceptos fundamentales para comprender la diversidad sexual y de género de manera respetuosa.")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🧬 Sexo")
            st.image(
                "https://plus.unsplash.com/premium_vector-1727956884275-8a8148de508c?q=80&w=880&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                caption="El sexo se asigna al nacer"
            )
            st.write(
                "Es la etiqueta que se nos asigna al nacer, generalmente por un doctor, basándose en nuestros genitales y cromosomas. "
                "Se registra en el certificado de nacimiento como “masculino” o “femenino”. "
            )

        with col2:
            st.subheader("🟣 Género")
            st.image(
                "https://images.unsplash.com/photo-1545693315-85b6be26a3d6?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                caption="El género es una construcción social"
            )
            st.write(
                "Es una construcción legal, social y cultural que establece normas, expectativas y roles sobre cómo deben comportarse las personas "
                "según su sexo asignado. "
            )

        st.divider()

        col3, col4 = st.columns(2)
        with col3:
            st.subheader("🧠 Identidad de género")
            st.image(
                "https://images.unsplash.com/photo-1605818363303-7073f9171de9?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                caption="Cómo te sientes contigo"
            )
            st.write(
                "Es cómo cada persona se siente y se percibe a sí misma en relación con el género. "
                "No está determinada por el cuerpo, sino por una experiencia interna y única. "
                "Esta identidad comienza a desarrollarse desde edades tempranas y forma parte central del sentido del yo."
                "Se expresa con la ropa, la voz, el lenguaje corporal y puede o no coincidir con el sexo asignado. "
            )

        with col4:
            st.subheader("💘 Orientación sexual")
            st.image(
                "https://images.unsplash.com/photo-1717700191408-35bb236d2cae?q=80&w=1183&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                caption="A quién te atrae"
            )
            st.write(
                "La orientación sexual es una atracción emocional, romántica, sexual o afectiva duradera hacia otros. "
                "Se distingue fácilmente de otros componentes de la sexualidad que incluyen sexo biológico, identidad sexual (el sentido psicológico de ser hombre o mujer) y el rol social del sexo (respeto de las normas culturales de conducta femenina y masculina). "
                "Entre las más comunes: homosexualidad, bisexualidad, asexualidad. "
            )

        st.success("✨ Todas las formas de identidad y orientación son válidas. ¡Vive con autenticidad y respeto!")




st.markdown("---")
st.header("📊 Evalúa tu experiencia")

# 1️⃣ Calificación de 1 a 5 estrellas
calificacion = st.slider("¿Qué tan útil fue la respuesta del chatbot?", 1, 5, 3)
st.write("⭐" * calificacion)

# 2️⃣ Comentario adicional
comentario = st.text_area("¿Tienes algún comentario o sugerencia?", placeholder="Escribe tu opinión aquí...")

# 3️⃣ Botón para 'enviar' (simulado)
if st.button("📩 Enviar evaluación"):
    st.success("¡Gracias por tu evaluación! 😊")
    if comentario:
        st.info("Tus comentarios nos ayudan a mejorar. ¡Gracias por compartirlos!")

# 4️⃣ Cierre amable
st.markdown("---")
st.markdown("Hecho con ❤️ por Zuleika Napurí •")
