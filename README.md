# CAS-ODK Overlay

This repository provides a **Copier-based overlay** for [Ontology Development Kit (ODK)](https://oboacademy.github.io/obook/tutorial/setting-up-project-odk/) projects.  
It extends the standard ODK scaffold with extra files, folders, and patterns that are automatically generated from **[Cell Annotation Schema (CAS)](https://github.com/obophenotype/cell-annotation-schema)** taxonomy JSON files.

## ✨ Features

- 📦 **ODK-compatible**: builds on top of a standard ODK project layout.  
- 🧬 **CAS-driven**: reads [CAS taxonomy JSON](https://github.com/obophenotype/cell-annotation-schema) to generate ontology terms and patterns.  
- ⚙️ **Templated**: uses [Copier](https://copier.readthedocs.io) and Jinja2 to render files/folders.  
- 🔁 **Re-renderable**: changes to your taxonomy or config can be applied repeatedly without breaking your repo.  
- 🧪 **Extensible**: supports custom Python preprocessing (pandas, rdflib, etc.) to derive variables for templates.  

## 🚀 Quickstart

1. **Create a base ODK project**  
   Follow the [ODK setup tutorial](https://oboacademy.github.io/obook/tutorial/setting-up-project-odk/).  
   Example:
   ```bash
   sh seed-via-docker.sh -C my-odk.yaml -c
   ```

2. **Apply this overlay with Copier**

   ```bash
   pip install copier
   copier copy gh:Cellular-Semantics/cas-odk-overlay .
   ```

3. **Provide inputs**

   * `src/data/taxonomy.json` → your CAS taxonomy file
   * `src/data/project.yaml` → minimal project metadata (ontology name, publications, species, etc.)

4. **Re-render when inputs change**

   ```bash
   copier update .
   ```

## 🛠️ Workflow

1. **Edit** `taxonomy.json` and `project.yaml`.
2. **Re-render** overlay (`copier update .`).
3. **Build ontology** with ODK:

   ```bash
   cd src/ontology
   sh run.sh make prepare_release
   ```
