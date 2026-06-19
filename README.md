# 🏛️ University

Repository containing assignments, reports, notes, study materials, and course
projects developed throughout my Computer Engineering degree, as well as
complementary cybersecurity training materials.

## 📚 Repository Structure

### 📐 Algebra Linear (`al`)

Linear Algebra course materials, including:

* Exercise lists
* Solutions
* Reference books and study materials

### ⚡ Circuitos Elétricos I (`circuitos-1`)

Materials related to the Electrical Circuits I course:

* Theoretical foundations
* Laboratory activities
* Exercise lists

### 📈 Equações Diferenciais Ordinárias (`edo`)

Assignments, notes, and materials related to Ordinary Differential Equations.

### 💼 Engenharia de Software (`eng-soft`)

Software Engineering coursework, reports, and exercise lists.

### 📏 Geometria Analítica (`ga`)

Analytic Geometry exercises and solutions.

### ☕ Programação Orientada a Objetos (`poo`)

Object-Oriented Programming assignments and projects.

### 🛡️ Hackers do Bem (`hackers-do-bem`)

Materials, exercises, labs, and reports from the Hackers do Bem program,
including:

* Fundamental Track
* Red Team Specialization

## 🎯 Purpose

This repository serves as:

* A centralized archive of academic work.
* A reference for future studies.
* A collection of solved exercises and reports.
* Documentation of practical activities performed during university courses and
  cybersecurity training.

## 📂 Organization

Most subjects follow a structure similar to:

```text
subject/
├── lista1
├── lista2
├── lista3
└── materiais
```

where each directory may contain:

* Source code
* Reports
* LaTeX documents
* PDFs
* Supporting materials

## 🛠️ LaTeX Workflow

Most LaTeX-based assignments include helper scripts to simplify editing and
compilation.

### `texcomp`

Compiles a LaTeX document into a PDF:

```bash
./texcomp main.tex
```

### `latexide`

Launches a lightweight LaTeX development environment by opening the source file
in `Neovim` and the generated PDF in `Zathura`. It also uses `entr` to
automatically recompile the document whenever the source file is saved.

```bash
./latexide main.tex
```

This workflow provides:

* Automatic recompilation after saving changes.
* Live PDF preview through Zathura.
* Editing with Neovim.
* Faster iteration when writing reports and assignments.

## 📑 License

This project is licensed under the Creative Commons License.

See the [LICENSE](LICENSE) file for details.
