from flask import Blueprint
from flask import render_template, request, jsonify 
from function import *

views = Blueprint(__name__,"views")
resultado = "Sin anemia"

@views.route("/")
def home():
    return render_template('home.html')

@views.route("/anemia")
def page_anemia():
    return render_template('paganemia.html')

@views.route("/cancerdemama")
def page_cancerdemama():
    return render_template('pagcancerdemama.html')

@views.route("/entrenamiento")
def page_entrenamiento():
    return render_template('pagentrenamiento.html')

#background process happening without any refreshing
@views.route('/background_process_test',methods=["POST"])
def background_process_test():
    sexo = request.form['sexo']
    input_edad = request.form['input_edad']
    input_rbc = request.form['input_rbc']
    input_pcv = request.form['input_pcv']
    input_mcv = request.form['input_mcv']
    input_mch = request.form['input_mch']
    input_mchc = request.form['input_mchc']
    input_rdw = request.form['input_rdw']
    input_tlc = request.form['input_tlc']
    input_plt = request.form['input_plt']
    lista_datos = [int(input_edad),int(sexo),float(input_rbc),float(input_pcv),float(input_mcv),float(input_mch),float(input_mchc),float(input_rdw),float(input_tlc),float(input_plt)]
    resultado_anemia = function_extern(lista_datos)
    print(resultado_anemia)
    
    return (resultado_anemia)

def function_extern(data):
    arreglodata = [data]
    return predictmodel_anemia('model_anemia_entrenado.pkl',arreglodata)


#background process happening without any refreshing
@views.route('/background_process_test_cancermama',methods=["POST"])
def background_process_test_cancermama():
    radio_med = request.form['radio_med']
    textura_med = request.form['textura_med']
    perimetro_med = request.form['perimetro_med']
    area_med = request.form['area_med']
    suavidad_med = request.form['suavidad_med']
    compacidad_med = request.form['compacidad_med']
    concavidad_med = request.form['concavidad_med']
    puntos_concavos_med = request.form['puntos_concavos_med']
    simetria_med = request.form['simetria_med']
    dimension_fractal_med = request.form['dimension_fractal_med']
    radio_sec = request.form['radio_sec']
    textura_sec = request.form['textura_sec']
    perimetro_sec = request.form['perimetro_sec']
    area_sec = request.form['area_sec']
    suavidad_sec = request.form['suavidad_sec']
    compacidad_sec = request.form['compacidad_sec']
    concavidad_sec = request.form['concavidad_sec']
    concavos_sec = request.form['concavos_sec']
    lista_datos = [float(radio_med),float(textura_med),float(perimetro_med),float(area_med),float(suavidad_med),float(compacidad_med),float(concavidad_med),float(puntos_concavos_med),float(simetria_med),float(dimension_fractal_med), float(radio_sec),float(textura_sec), float(perimetro_sec),float(area_sec), float(suavidad_sec),float(compacidad_sec), float(concavidad_sec),float(concavos_sec)]
    resultado_cancermama = function_extern_cancermama(lista_datos)
    
    return ("Funciona prueba cancer mama")

def function_extern_cancermama(data):
    arreglodata = [data]
    return predictmodel_cancermama('model_cancermama_entrenado.sav',arreglodata)