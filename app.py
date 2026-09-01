import streamlit as st

st.title("📚 StudyTrack")
st.write("Analiza tus hábitos y recibe recomendaciones para organizar mejor tu tiempo.")

st.divider()

st.header("📝 Ingresa tus hábitos")

horas_estudio = st.number_input(
    "¿Cuántas horas estudias al día?",
    min_value=0.0,
    max_value=12.0,
    value=2.0,
    step=0.5
)

horas_sueno = st.number_input(
    "¿Cuántas horas duermes al día?",
    min_value=0.0,
    max_value=15.0,
    value=8.0,
    step=0.5
)

tiempo_pantalla = st.number_input(
    "¿Cuántas horas utilizas pantallas al día?",
    min_value=0.0,
    max_value=16.0,
    value=4.0,
    step=0.5
)

deporte = st.selectbox(
    "¿Practicas deporte?",
    ["Sí", "No"]
)

st.divider()

if st.button("🔎 Analizar mis hábitos"):

    puntos = 0
    recomendaciones = []

    if horas_estudio >= 3:
        puntos += 1
    else:
        recomendaciones.append(
            "Intenta aumentar progresivamente tus horas de estudio."
        )

    if horas_sueno >= 7:
        puntos += 1
    else:
        recomendaciones.append(
            "Procura tener un horario de descanso más regular."
        )

    if tiempo_pantalla <= 5:
        puntos += 1
    else:
        recomendaciones.append(
            "Intenta reducir el tiempo de pantalla."
        )

    if deporte == "Sí":
        puntos += 1
    else:
        recomendaciones.append(
            "Considera incluir actividad física en tu rutina."
        )

    st.header("📊 Resultado")

    if puntos == 4:
        st.success("¡Excelente! Tus hábitos presentan un buen equilibrio.")
    elif puntos >= 2:
        st.warning("Tus hábitos son aceptables, pero hay aspectos que puedes mejorar.")
    else:
        st.error("Tus hábitos tienen varios aspectos que podrías mejorar.")

    st.write(f"**Puntuación de hábitos: {puntos}/4**")

    st.subheader("💡 Recomendaciones")

    if recomendaciones:
        for recomendacion in recomendaciones:
            st.write("• " + recomendacion)
    else:
        st.write("No tenemos recomendaciones adicionales.")

    st.subheader("📋 Tus datos")

    datos = {
        "Horas de estudio": horas_estudio,
        "Horas de sueño": horas_sueno,
        "Tiempo de pantalla": tiempo_pantalla
    }

    st.bar_chart(datos)
