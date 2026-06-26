# Script for Fill Certificate Names

Leia isso em [Português - BR](https://github.com/filhaDeHades/Fill-Out-Certificate/blob/main/README-pt-br.md).

This repository was created for the automatizating the issue of certificates from organized events. This process, otherwise would be slow and tedious.

# How to use it:

In the repository you will find all the files necessary por you to test the script.

- **Certificate Model:**
The model (modelo-certificado.jpg) can be used as a base for the creation of your on certificate (Using the same height por the participant name). That way you won't need to do any alteration on the code.

In the case use a model with a different height for the name, you can simply change the constant ``NAME_HEIGHT`` on top of the file (for better aesthetics it's recommended that you subtract 2 pixels from the real height).

Also it's recommended that you use a JPG our JPEG file for your model. In case you preffer a PNG file it will be needed to make the convertion from RGBA to RGB.

- **Arquivo de Input:**
The input file was the name of the model to be used in the first line. The name of the people you are filling the certificates for must be in the next lines (**one name for line**).
