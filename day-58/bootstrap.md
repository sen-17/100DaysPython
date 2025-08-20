# 📘 Bootstrap Notes

## 📌 What is Bootstrap?

* Open-source **CSS framework** with pre-made CSS files.
* Helps speed up UI development with ready-to-use classes and components.
* Can be included in your project easily via **CDN** `<link>` tag.
* Great for rapid development, but **not ideal for highly complex custom controls**.

---

## 📐 Bootstrap Grid (12-Column System)

Basic structure always follows **container → row → columns**:

```html
<div class="container">
  <div class="row">
    <div class="col">Hello</div>
  </div>
</div>
```

### ✅ Key Points:

* `.container` is **responsive** → multiple types:

  * `container-sm`, `container-md`, `container-lg`, `container-xl`, `container-xxl`, `container-fluid`
* `.row` groups columns
* `.col` → auto-fit equal width columns
* `.col-*` → manually sized columns e.g.:

```html
<div class="container">
  <div class="row">
    <div class="col-2">Hello</div>
    <div class="col-4">Hello</div>
    <div class="col-6">Hello</div>
  </div>
</div>
```

---

## 🔁 Breakpoints & Responsive Columns

* Bootstrap uses **breakpoints**:
  `sm`, `md`, `lg`, `xl`, `xxl`

Use multiple breakpoints to control column size based on screen width:

```html
<div class="col-sm-12 col-md-8 col-lg-4">
```

Means:

* On **small** devices → width = 12/12 (full width)
* **Medium** → 8/12
* **Large** → 4/12

---

## 🧩 Bootstrap Components

Reusable pre-designed UI elements:

* **Buttons:** `btn-primary`, `btn-secondary`, `btn-danger`, etc.
* **Cards**
* **Navs**
* **Utilities: spacing, display, etc.**

### Spacing Utilities:

* `m` = margin, `p` = padding
* Directions: `t` (top), `b` (bottom), `x` (left & right), `y` (top & bottom)
* Example: `mt-5` → margin-top 5, `my-3` → margin-top & bottom 3

---

## 🌙 Dark Mode

Enable dark mode by adding:

```html
<html data-bs-theme="dark">
```


