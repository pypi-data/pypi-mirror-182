import abc
import jsonpickle
import numpy as np
import pickle
from typing import Any, Optional, Dict, List

from galleries import files_utils
from galleries.annotations_filtering.filter import FilterStatement


class IGallery(abc.ABC):
	"""
	Interfaz para implementar el acceso a una galería de imágenes y sus anotaciones
	"""

	@abc.abstractmethod
	def get_name(self) -> str:
		"""
		Get the gallery's name
		:return:
		"""
		pass

	@abc.abstractmethod
	def set_name(self, name: str):
		"""
		set the gallery's name
		:return:
		"""
		pass

	@abc.abstractmethod
	def get_indices(self, filters: List[List[FilterStatement]] = None):
		"""
		Obtener los índices de las imágenes. Estos índices son utilizados después para obtener información de la imagen.
		Un índice puede ser, por ejemplo, la dirección de la imagen en el sistema de ficheros local.
		:return:
		"""
		pass

	@abc.abstractmethod
	def get_annotations_by_index(self, img_index) -> dict:
		"""
		Get an image annotations based on its index.
		:param img_index:
		:return:
		"""
		pass

	@abc.abstractmethod
	def get_image_by_index(self, index: Any) -> np.ndarray:
		"""
		Get an image based on an index.
		:param index:
		:return:
		"""
		pass

	@abc.abstractmethod
	def get_annotations_types(self) -> Optional[Dict[str, type]]:
		"""
		Returns a dictionary of each annotation's type. Also, you can get all annotations names from the
		dictionary's keys. Returns None if annotations names and types are unknown.
		:return:
		"""
		pass

	@abc.abstractmethod
	def get_discrete_annotations_values(self) -> Dict[str, list]:
		"""
		Returns, for each annotation, a list of possible values. Only for annotations that have a finite
		set of possible values.
		:return:
		"""
		pass

	def get_indices_annots(self, filters: List[List[FilterStatement]] = None):
		for img_index in self.get_indices(filters):
			yield img_index, self.get_annotations_by_index(img_index)

	def get_images(self, filters: List[List[FilterStatement]] = None):
		for img_index in self.get_indices(filters):
			yield self.get_image_by_index(img_index)

	def get_images_annots(self, filters: List[List[FilterStatement]] = None):
		for img_index, annots in self.get_indices_annots(filters):
			img = self.get_image_by_index(img_index)
			yield img, annots

	def get_images_by_indices(self, indices: List[Any]):
		for index in indices:
			yield self.get_image_by_index(index)

	def get_annotations_by_indices(self, indices: List[Any]):
		for index in indices:
			yield self.get_annotations_by_index(index)

	def get_images_and_annotations_by_indices(self, indices: List[Any]):
		for index in indices:
			image = self.get_image_by_index(index)
			annotations = self.get_annotations_by_index(index)
			yield image, annotations

	@staticmethod
	def write_gallery(gallery: 'IGallery', file_path: str, nice_format=False):
		if nice_format:
			serializer = jsonpickle
			file_mode = 'w'
		else:
			serializer = pickle
			file_mode = 'wb'
		files_utils.create_dir_of_file(file_path)
		with open(file_path, file_mode) as file:
			data = serializer.dumps(gallery)
			file.write(data)

	@staticmethod
	def read_gallery(file_path: str, nice_format=False) -> 'IGallery':
		if nice_format:
			serializer = jsonpickle
			file_mode = 'r'
		else:
			serializer = pickle
			file_mode = 'rb'
		with open(file_path, file_mode) as file:
			data = file.read()
			gallery = serializer.loads(data)
		return gallery
