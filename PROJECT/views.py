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
    radio_med = request.form["radio_med"]
    textura_med = request.form['textura_med']
    perimetro_med = request.form['perimetro_med']
    area_med = request.form['area_med']
    suavidad_med = request.form['suavidad_med']
    compacidad_med = request.form['compacidad_med']
    concavidad_med = request.form['concavidad_med']
    puntos_concavos_med = request.form['puntos_concavos_med']
    simetria_med = request.form['simetria_med']
    dimension_fractal_med = request.form['dimension_fractal_med']
    radio_se = request.form['radio_se']
    textura_se = request.form['textura_se']
    perimetro_se = request.form['perimetro_se']
    area_se = request.form['area_se']
    suavidad_se = request.form['suavidad_se']
    compacidad_se = request.form['compacidad_se']
    concavidad_se = request.form['concavidad_se']
    concavos_se = request.form['concavos_se']
    simetria_se = request.form['simetria_se']
    dimension_fractal_se = request.form['dimension_fractal_se']
    radio_worst = request.form['radio_worst']
    textura_worst = request.form['textura_worst']
    perimetro_worst = request.form['perimetro_worst']
    area_worst = request.form['area_worst']
    suavidad_worst = request.form['suavidad_worst']
    compacidad_worst = request.form['compacidad_worst']
    concavidad_worst = request.form['concavidad_worst']
    concavos_worst = request.form['concavos_worst']
    simetria_worst = request.form['simetria_worst']
    dimension_fractal_worst = request.form['dimension_fractal_worst']
    lista_datos = [float(radio_med),float(textura_med),float(perimetro_med),float(area_med),float(suavidad_med),float(compacidad_med),float(concavidad_med),float(puntos_concavos_med),float(simetria_med),float(dimension_fractal_med),
                    float(radio_se),float(textura_se), float(perimetro_se),float(area_se), float(suavidad_se),float(compacidad_se), float(concavidad_se),float(concavos_se),
                    float(simetria_se),float(dimension_fractal_se), float(radio_worst),float(textura_worst), float(perimetro_worst),float(area_worst), float(suavidad_worst),float(compacidad_worst),
                    float(concavidad_worst),float(concavos_worst), float(simetria_worst),float(dimension_fractal_worst)]
    resultado_cancermama = function_extern_cancermama(lista_datos)
    
    return (resultado_cancermama)

def function_extern_cancermama(data):
    arreglodata = [data]
    return predictmodel_cancermama('model_cancermama_entrenado.sav',arreglodata)