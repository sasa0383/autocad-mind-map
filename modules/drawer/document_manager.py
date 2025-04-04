import ezdxf

class DocumentManager:
    def __init__(self, filename=None):
        """
        Initialize the DocumentManager.

        Args:
            filename (str): Default filename for saving the document.
        """
        self.doc = ezdxf.new()
        self.msp = self.doc.modelspace()
        self.filename = filename

    def get_modelspace(self):
        """
        Get the modelspace of the document.

        Returns:
            modelspace: DXF modelspace.
        """
        return self.msp

    def save_document(self, filename=None):
      file_to_save = filename or self.filename
      print(f"Saving DXF document to {file_to_save}")
      self.doc.saveas(file_to_save)
