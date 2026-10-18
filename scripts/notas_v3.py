#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E6 v3 · Contenido agregado a la presentación del Consejo Universitario a pedido del
Rectorado (archivo «AGREGAR NOTAS EXPLICATIVAS Y ABREVIATURAS…PPTX»):
  1) Notas explicativas del expositor (speaker notes) para las 32 láminas.
  2) Lámina nueva «Siglas y abreviaturas de la exposición» (pos. 3).
  3) Guía de lectura de la lámina ROM (G-13 re-etiquetada por capítulo).
El orden de NOTES corresponde al mazo v3 de 32 láminas (glosario insertado en pos. 3)."""

# --------------------------------------------------------------------- 1. NOTAS DEL EXPOSITOR
NOTES = [
    # 1 Portada
    "Saludo al Consejo Universitario y al Cap. Alt. / Dr. Guillermo Antonio Riut Hernández, "
    "Rector. Se presenta el Proyecto 04 del Plan Maestro UMC 2025–2030: restauración de la "
    "Torre de Observación / Puente de Mando y de la Sala Técnica de Investigación "
    "Hidrometeorológica, tras el doblete sísmico del 24-06-2026. Expediente "
    "UMC2030-P04-TOBSHM-R02, nivel INGENIERÍA BÁSICA / ANTEPROYECTO: sirve para decidir y "
    "contratar, no para construir. Los cinco indicadores del encabezado resumen el caso: "
    "106,00 m² de intervención, coronación +22,02 m, dos edificaciones patrimoniales, ≈ 30 "
    "meses y una estimación ROM de 2,09–3,25 MUSD.",
    # 2 Cómo leer
    "Antes de entrar en materia, fije el marco de lectura: qué ES y qué NO es este documento. "
    "ES ingeniería básica para decidir programa, geometría, diagnóstico, inversión, plazos y "
    "riesgos, y para contratar levantamiento, geotecnia, inspección estructural e ingeniería de "
    "detalle. NO es proyecto ejecutivo ni presupuesto de licitación, y no sustituye permisos ni "
    "la autorización del órgano de patrimonio. Todo lo no verificado está registrado como RFI; "
    "pediremos al Consejo ordenar su cierre.",
    # 3 Siglas (nueva)
    "Lámina de referencia rápida añadida a pedido del Rectorado: recoja aquí las siglas que "
    "aparecerán durante la exposición (ROM, RFI, NPT, AWS, HBIM, MEP, OS2, entre otras). Puede "
    "pasarse en diez segundos anunciando que queda como anexo de lectura, pero conviene "
    "mencionar las tres críticas: ROM = estimación de orden de magnitud con banda −25 %/+40 %; "
    "RFI = información pendiente que el Consejo debe ordenar cerrar; NPT = nivel de piso "
    "terminado, referencia de todas las cotas.",
    # 4 Agenda
    "Seis bloques en ≈ 20 minutos: contexto patrimonial y sísmico (5–7), el conjunto y su "
    "programa (8–12), diagnóstico y doctrina (13–15), ingeniería (16–22), inversión, plazos y "
    "riesgos (23–29) y cierre con la condición de emisión y los acuerdos solicitados (30–32). "
    "Anuncie desde ya que la última lámina contiene cuatro acuerdos concretos que se someten a "
    "aprobación.",
    # 5 Marco
    "El Plan Maestro UMC 2025–2030 declara doce proyectos estratégicos; este es el cuarto y "
    "restaura el conjunto patrimonial del Área Cultural. Se coordina en un único modelo de "
    "implantación con P01 (Torre A–STCW), P02 (Torre B–CDP) y P03 (Vicerrectorado); los "
    "corredores tecnológico y de redes son infraestructura común que este proyecto NO "
    "modifica. La figura G-02 resume la línea documental 1951→2026. Autoría del documento "
    "fuente: Prof. Jhonny Da Silva Izquierdo (MSc. Ing. Lic.).",
    # 6 Patrimonio
    "La Torre nace con la Escuela Náutica de Venezuela de Luis Malaussena (MOP, c. 1951–1958): "
    "no es un añadido, es parte del valor del conjunto. La fotografía histórica del archivo MOP "
    "muestra la torre original de 12,20 m con su personal: esa imagen justifica la doctrina de "
    "restauración que veremos en la lámina 14. El expediente documenta 198 páginas y 487 "
    "fotografías del inventario Portaplanos 01–05.",
    # 7 Doblete
    "El 24-06-2026 un doblete M7,2 + M7,5 golpeó la costa y el campus: el fotograma de la "
    "evacuación, aportado por la comunidad universitaria, es la evidencia vivencial del evento. "
    "El daño se concentra en las edificaciones patrimoniales: colapso parcial en N0 y pérdida "
    "de coronación en la Torre. Este hecho convierte la restauración en urgencia institucional, "
    "no en obra discrecional.",
    # 8 Implantación
    "Con la figura G-01 ubique al Consejo: la Torre se adosa al Auditorio del Área Cultural; la "
    "Sala Técnica es una edificación separada a 3,61 m, unida por junta estructural y de "
    "servicios; la plaza de honor opera como explanada de protocolo y punto de reunión R-1 del "
    "plan de evacuación. Nada de esto altera la implantación general del Plan Maestro.",
    # 9 Emblema
    "Lámina emocional del mazo: la Torre iluminada sobre la plaza de honor es el emblema "
    "vigente de la UMC. El balizamiento escénico existente se conserva y se recablea porque "
    "forma parte del uso ceremonial documentado (actos, grados, fiestas patrias). Compare con "
    "la foto histórica de la lámina 6: misma composición, setenta años después. Ese es el valor "
    "que el proyecto protege y restituye.",
    # 10 Torre
    "Ficha técnica de la Torre UMC-T-CUL-TOO-02: cinco niveles de 13,50 m² (3,60 × 3,75 m), "
    "67,50 m² totales, puente de mando en N4. Altura de coronación adoptada: +22,02 m sobre NPT "
    "±0,000, según precedencia documental 8.DF.2.362 No. 149; la cota de 12,20 m quedó ANULADA "
    "por 15 DF 30 y 15,80 m corresponde a una alternativa RFI-ALT-01 aún abierta para "
    "verificación física.",
    # 11 Niveles
    "Recorra el programa con el cuadro por niveles: N0 acceso y técnico, N1–N2 oficinas y "
    "registro, N3 laboratorio, N4 puente de mando con visuales 360°. Las áreas netas y brutas "
    "cuadran con el cuadro de programa del capítulo 8 del expediente; la escalera única es el "
    "caso crítico de evacuación que se trata en la lámina 23.",
    # 12 Sala
    "La Sala Técnica UMC-S-ACA-STH-15 alberga la estación hidrometeorológica: 38,50 m² útiles "
    "adoptados frente a los 40,00 m² de programa (desviación −3,75 % aceptada y registrada como "
    "RFI-ARE-01). Zona de servidores con precisión 18–27 °C / 40–60 % HR, puesto de observación "
    "y abrigo tipo Stevenson exterior en parcela propia.",
    # 13 Diagnóstico
    "Diagnóstico patológico preliminar post-sísmico con la escala referencial D0–D5: colapso "
    "parcial D4–D5 en N0 y coronación, fisuración D2–D3 en machones de niveles intermedios. "
    "Importante: es un diagnóstico PRELIMINAR sobre registro fotográfico; la inspección "
    "estructural detallada no se ha realizado y es condición suspensiva (RFI-PAT-01). No "
    "afirmar ante el Consejo que la estructura ya fue inspeccionada.",
    # 14 Doctrina
    "Doctrina de intervención patrimonial en cinco verbos: conservar, consolidar, reintegrar, "
    "reponer, retirar. Consolidar la materialidad de 1951–1958 siempre que el diagnóstico lo "
    "permita; reintegrar con distinguibilidad (lo nuevo se lee como nuevo); retirar solo con "
    "desmontaje por elementos, acta y trazabilidad. La precedencia documental verificada en "
    "archivo sustenta la vigencia de 8.DF.2.362 (22,02 m).",
    # 15 Concepto
    "«El Vigía de la Memoria»: la misma vertical que sostiene el puente de mando sostiene el "
    "mástil de instrumentos. Volumen prismático esbelto de hormigón visto, bandas horizontales "
    "blancas y vidriado azul-verde de control solar: el lenguaje del conjunto de Malaussena, no "
    "un gesto ajeno. Coronamiento técnico plano con asta, pararrayos y antenas.",
    # 16 Estructura
    "Criterios estructurales de anteproyecto: pórticos de hormigón armado sobre pilotes y "
    "cabezales existentes; encamisado de 96 m² en N0–N2 y disipación en niveles altos; diseño "
    "por secuencia sísmica porque el segundo evento actuó sobre estructura ya fisurada; "
    "verificación de viento y fatiga de la unión asta-coronación en el puente de mando. Todo "
    "pendiente de cálculo ejecutivo.",
    # 17 MEP
    "Instalaciones: 45 kVA estimados con TGBT y ATS; UPS de 10 kVA exclusivo para "
    "instrumentación y registro; sala de servidores con precisión y redundancia N+1. El "
    "pararrayos lleva bajante dedicada en el asta, separada de las redes de datos según IEC "
    "62305 — esta separación se detalla en las láminas 19 y 20. PCI: detección en todos los "
    "niveles e hidrante del anillo en la plaza.",
    # 18 Instrumentación
    "La estación como infraestructura crítica: mástil de 10,00 m con anemómetro y veleta, "
    "abrigo tipo Stevenson y parcela de sensores; datalogger con registro local y replicación "
    "al CDP (Torre B) por fibra OS2; control de calidad con metadatos y certificados de "
    "calibración. La serie histórica desde 1975 se migra y publica como activo institucional "
    "(RFI-MET-01).",
    # 19 U1 azotea y canalizaciones
    "Lámina incorporada por el equipo técnico con dos decisiones de obra por definir: (1) el "
    "anclaje del mástil a la losa —base de placa de acero con pernos de expansión versus "
    "sistema de vientos o tensores para las cargas de viento en altura—; y (2) la canalización "
    "vertical desde el datalogger en azotea, bajando los cinco pisos por tubería EMT o PVC "
    "pesado hasta la caja de empalme que conecta con el backbone de fibra hacia el CDP. Ambas "
    "quedan como RFI de ingeniería de detalle.",
    # 20 U2 notas de instalación
    "Notas de instalación en obra, de cumplimiento estricto: prohibido compartir bandejas, "
    "ductos o pasamuros entre la bajante del pararrayos (cobre desnudo de 50 mm² o pletina "
    "equivalente) y los conduit EMT que portan la fibra OS2 y las señales meteorológicas. Las "
    "mallas de tierra, aunque corren separadas los cinco pisos, se unen en el subsuelo mediante "
    "electrodo de chispa (spark gap): referencia común solo ante descargas masivas, sin bucles "
    "de tierra destructivos.",
    # 21 U3 red y telemetría
    "Arquitectura de red del campus (figura G-10): IDF/MMR en la Sala, backbone de fibra OS2 "
    "hasta el CDP de Torre B, replicación del dato meteorológico con ciberseguridad y respaldo, "
    "e integración con los sistemas institucionales (CCTV, acceso, VTS). La estación publica "
    "dato continuo aunque falle el enlace local: el datalogger conserva registro autónomo.",
    # 22 Industria 5.0
    "Patrimonio monitorizado, no museificado: escaneo láser y fotogrametría de lo existente "
    "antes de cualquier demolición; modelo federado en CDE con estados 01–04 y codificación "
    "UMC-T / UMC-S; acelerómetros e inclinómetros en N2 y coronación tras el doblete. Enfoque "
    "humanocéntrico: la tecnología apoya la observación manual del guardiamarina, no la "
    "sustituye.",
    # 23 Accesibilidad
    "El caso crítico: una sola escalera. Aforo de diseño 20 personas en el puente de mando y "
    "5–10 en la Sala; plataforma elevadora accesible que NO sustituye rutas de evacuación; "
    "compensaciones —área de refugio en N2, comunicación por voz, emergencia redundante y "
    "protocolo de desalojo previo a actos con aforo completo—. El cálculo de recorrido y ancho "
    "confirmará la solución o exigirá segunda salida (RFI-PRO-01).",
    # 24 Exteriores
    "Obras exteriores: 380 m² de plaza de honor, banda de protocolo y drenaje. La Fracción 1 se "
    "interviene como una sola unidad: un levantamiento, un modelo HBIM, una matriz de daño y "
    "una cronología coordinada con el Aula Magna. Condición suspensiva expresa: no se inicia "
    "obra del Área Cultural sin levantamiento y diagnóstico completos de la Fracción 1.",
    # 25 Especificaciones
    "28 capítulos de especificación técnica y un BOQ Rev.0 derivado directamente de la "
    "geometría adoptada: 96 m² de encamisados, 40,50 m² de losas recreadas, 129 m² de "
    "cerramientos repuestos, 35 m³ de escombros patrimoniales, 380 m² de exteriores y la "
    "estación completa como partida de bienes muebles con especificación por fabricante.",
    # 26 ROM
    "Lámina clave de inversión — explique la figura G-13 con calma: CADA BARRA HORIZONTAL ES UN "
    "CAPÍTULO DEL PRESUPUESTO, numerado del 1 al 9 con su nombre a la izquierda. El tramo azul "
    "oscuro va del cero al costo mínimo (−25 %); el tramo azul claro continúa hasta el máximo "
    "(+40 %); el rombo rojo marca el punto medio; la cifra a la derecha es el rango en kUSD. "
    "Ejemplo: la barra 6, instrumentación meteorológica, vale entre 220 y 420 kUSD y es la de "
    "mayor varianza: se licitará por desempeño. La suma de los nueve capítulos da el total ROM "
    "2.090–3.250 kUSD. Repita: NO es presupuesto de licitación.",
    # 27 Programación
    "≈ 30 meses con seis gates de control G0–G6: Fase A (4 meses) cierra la información de "
    "campo —TLS, patología, geotecnia, topografía—; fases B y C solapan ingeniería, "
    "autorización patrimonial y licitación; fase D (12 meses) concentra la obra. La estación "
    "provisional se instala en el mes 1 para no interrumpir la serie histórica: dato continuo "
    "durante toda la obra.",
    # 28 Riesgos
    "Matriz de riesgos del capítulo 25.1 con tratamiento explícito: réplica sísmica durante la "
    "obra (apuntalamiento y monitoreo desde el mes 1); geotecnia y pilotes sin verificar "
    "(campaña en Fase A, condición suspensiva); precedencia documental y tres alturas "
    "(verificación archivística y física, RFI-ALT-01); pérdida de piezas en el desescombro "
    "(desmontaje con acta y trazabilidad). Ningún riesgo queda sin dueño ni sin acción.",
    # 29 RFI
    "Dieciséis RFI abiertas en R02; las críticas para el Consejo: ALT-01 (altura de coronación), "
    "GEO-001/002 (posición y altimetría), GEOT-01 (pilotes), PAT-01 (inspección detallada), "
    "DOC-01 (precedencia) y PRO-01 (segunda salida). Pedir al Consejo ORDENAR su cierre con "
    "responsables y fechas: son la condición para pasar de anteproyecto a ingeniería de "
    "detalle.",
    # 30 Condición de emisión
    "Transparencia ante el órgano de decisión: lo que NO está definido (geotecnia, cálculo "
    "estructural, memorias firmadas, BM altimétrico) frente a lo que SÍ está definido con "
    "precisión (programa verificado, geometría justificada por precedencia, doctrina "
    "patrimonial, ROM Clase 5, cronograma y riesgos). El proyectista responsable se designará "
    "según la Ley de Ejercicio de la Ingeniería; uso institucional UMC – Marina Mercante de "
    "Venezuela.",
    # 31 Acuerdos
    "Cierre operativo: cuatro acuerdos que se someten a resolución del Consejo: (1) APROBAR el "
    "expediente R02 como base de ingeniería básica para contratar levantamiento, geotecnia, "
    "inspección e ingeniería de detalle; (2) ORDENAR el cierre de las RFI críticas con "
    "responsables y fechas; (3) AUTORIZAR la Fase A y la estación provisional en el mes 1; "
    "(4) DESIGNAR la unidad de gerencia y al proyectista responsable. Lea los cuatro en voz "
    "alta y solicite votación.",
    # 32 Cierre
    "Cierre con la imagen-síntesis: dos edificaciones patrimoniales, una sola intervención; la "
    "ceremonia y la medición, 1951→2030. Agradezca al Rectorado el registro fotográfico "
    "institucional y abra la ronda de preguntas teniendo a mano las láminas 10 (alturas), 26 "
    "(ROM) y 29 (RFI), que son las que suelen concentrar las consultas del Consejo.",
]

# --------------------------------------------------------------------- 2. GLOSARIO (lámina 3)
GLOSARIO_IZQ = [
    "AIM — Asset Information Model: modelo de información de activos",
    "AWS — Automatic Weather Station: estación meteorológica automática",
    "BMS / EMS — Building / Energy Management System",
    "BOQ — Bill of Quantities: cómputos y presupuesto derivado",
    "CDP — Centro de Datos Principal (Torre B, Proyecto 02)",
    "CCTV — Circuito cerrado de televisión (seguridad electrónica)",
    "CDE — Common Data Environment: entorno común de datos BIM",
    "D0–D5 — Grados de la escala referencial de daño post-sísmico",
    "EMT — Electrical Metallic Tubing: tubería conduit metálica",
    "FV / BESS — Fotovoltaico / Battery Energy Storage System",
    "G-nn — Figura del expediente (p. ej. G-13: estimación ROM)",
    "HBIM — Heritage BIM: modelado de información del patrimonio",
    "HVAC — Calefacción, ventilación y aire acondicionado",
    "IDF / MMR — Distribuidor principal de TIC / sala de interconexión",
    "IEC — International Electrotechnical Commission (normas)",
    "IMG-CU-nn — Fotografía institucional UMC del anexo D",
]
GLOSARIO_DER = [
    "ILV — Iluminación y ventilación natural",
    "kUSD / MUSD — Miles / millones de dólares de los EE. UU.",
    "MEP — Mecánica, electricidad y plomería (instalaciones)",
    "METAR — Informe meteorológico aeronáutico rutinario",
    "MOP — Ministerio de Obras Públicas (archivo 1951, Malaussena)",
    "NPT — Nivel de Piso Terminado (NPT ±0,000: cota de referencia)",
    "OMM — Organización Meteorológica Mundial",
    "OS2 — Fibra óptica monomodo (backbone exterior)",
    "PCI — Protección Contra Incendios",
    "RFI — Request for Information: información pendiente (16 en R02)",
    "ROM — Rough Order of Magnitude: estimación Clase 5 (−25 %/+40 %)",
    "STCW — Convenio de formación y guardia de la gente de mar",
    "TLS — Terrestrial Laser Scanning: escaneo láser terrestre",
    "UPS / ATS — Respaldo ininterrumpido / conmutador de transferencia",
    "VTS — Vessel Traffic Service: servicio de tráfico marítimo",
    "UMC — Universidad Marítima del Caribe",
]

# --------------------------------------------------------------------- 3. LECTURA DE LA ROM
ROM_GUIA = [
    "Cada barra horizontal ES un capítulo del presupuesto: su nombre y número están a la "
    "izquierda de la barra (1 Estudios previos … 9 Ingeniería y contingencia).",
    "Tramo azul oscuro: del cero al costo MÍNIMO estimado (escenario −25 %).",
    "Tramo azul claro: del mínimo al costo MÁXIMO estimado (escenario +40 %).",
    "Rombo rojo: punto medio del rango · Cifra «a – b kUSD»: rango del capítulo en miles de "
    "USD (p. ej. barra 6, instrumentación: 220 – 420 kUSD).",
    "La suma de los nueve capítulos da el TOTAL ROM: 2.090 – 3.250 kUSD (AACE Clase 5). No es "
    "presupuesto de licitación.",
]
ROM_NOTA = ("Cómo leer la figura: cada barra es un capítulo del presupuesto (nombre a la "
            "izquierda); el tramo oscuro llega al mínimo (−25 %) y el claro al máximo (+40 %), "
            "en kUSD. La instrumentación meteorológica concentra la mayor varianza y se "
            "licitará por desempeño.")

# Renglonnes actualizados de la agenda (orden v3 de 32 láminas)
AGENDA = [["1", "Marco, patrimonio y evento sísmico", "5 – 7"],
          ["2", "El conjunto: implantación y programa", "8 – 12"],
          ["3", "Diagnóstico y doctrina de intervención", "13 – 15"],
          ["4", "Ingeniería: estructura, MEP, instrumentación, redes, Industria 5.0", "16 – 22"],
          ["5", "Accesibilidad, exteriores, especificaciones, inversión, plazos y riesgos",
           "23 – 29"],
          ["6", "Condición de emisión y acuerdos solicitados", "30 – 32"]]
