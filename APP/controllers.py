import mimetypes
from flask import Blueprint, current_app, request, jsonify,url_for,send_from_directory, abort
from .service import create_product,get_all_productos
from werkzeug.utils import secure_filename
import os
import json

product_bp = Blueprint('product_bp', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@product_bp.route('/producto/guardar-con-imagen', methods=['POST'])
def add_product_with_image():
    if 'file' not in request.files:
        return jsonify({'message': 'No se ha proporcionado ningún archivo'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No se ha seleccionado ningún archivo'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        file_url = url_for('product_bp.uploaded_file', filename=filename, _external=True, _scheme='http')

        producto_json = request.form.get('producto')
        producto_data = json.loads(producto_json)

        new_product = create_product(
            nombreproducto=producto_data['nombreproducto'],
            precioproducto=float(producto_data['precioproducto']),
            detalleproducto=producto_data['detalleproducto'],
            ivaproducto=float(producto_data['ivaproducto']),
            urlImagen=file_url,
            sistema=producto_data['sistema']
        )

        product_dict = new_product.to_dict()

        return jsonify({'message': 'Producto creado exitosamente', 'product': product_dict}), 201

    return jsonify({'message': 'Formato de archivo no permitido'}), 400

@product_bp.route('/producto/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

""" @product_bp.route('/producto/<filename>',methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@product_bp.route('/uploads/<filename>', methods=['GET'])
def uploaded_file2(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
 """
#metodo para obtener productos
@product_bp.route('/producto/listar', methods=['GET'])
def get_products():
    products = get_all_productos()
    return jsonify(products)


""" @product_bp.route('/productos/<filename>', methods=['GET'])
def get_product_image(filename):
    # Verificar si el archivo existe en el directorio de carga
    path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.isfile(path):
        abort(404)  # Devolver un error 404 si el archivo no existe

    # Obtener el tipo MIME del archivo
    mime_type, _ = mimetypes.guess_type(filename)

    # Si no se puede determinar el tipo MIME, usar un valor predeterminado
    if mime_type is None:
        mime_type = 'application/octet-stream'

    # Devolver la imagen como un archivo adjunto
    return send_from_directory(UPLOAD_FOLDER, filename, mimetype=mime_type)
 """