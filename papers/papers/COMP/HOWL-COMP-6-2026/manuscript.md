# SIML - Silo Markup Language (TOML Format)

## The Vision

**Registry:** [@HOWL-COMP-6-2026]

**Series Path:** [@HOWL-COMP-1-2026] → [@HOWL-COMP-2-2026] → [@HOWL-COMP-3-2026] → [@HOWL-COMP-4-2026] → [@HOWL-COMP-5-2026] → [@HOWL-COMP-6-2026]

**Parent Framework:** [@HOWL-COMP-1-2026]

**DOI:** 10.5281/zenodo.18676935

**Date:** February 2026

**Domain:** Software Architecture / Systems Engineering / Real-Time Computing

**Status:** Architectural Blueprint for Independent Implementation

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude 4.5 Sonnet. 

---

**Silo is not "the web, but better."**

**Silo is the successor to the web.**

Like:
- Email → Slack (protocols replaced)
- Forums → Reddit (platforms replaced)
- Geocities → Dead... until now

**Silo Web = Geocities Reborn**

---

## 1. Why TOML?

**TOML = Tom's Obvious Minimal Language**

**Properties:**
- Human-readable (like INI files)
- Simple syntax (no ambiguity)
- Hierarchical (tables and nested tables)
- Typed (strings, numbers, booleans, arrays)
- Comments (`#`)
- Widespread (used by Rust, Python, many tools)

**Perfect for SIML because:**
- No parsing ambiguity
- Easy to hand-write in Notepad
- Easy to parse (many libraries)
- Natural mapping to structs
- Comments for documentation

---

## 2. SIML in TOML Format

### 2.1 Basic Structure

```toml
# website.siml - Complete site definition

[site]
name = "My Shop"
version = "1.0"
author = "Solo Dev"
active_theme = "dark"

# ============================================================================
# THEMES
# ============================================================================

[theme.dark]
background = [20, 20, 20]
text = [240, 240, 240]
primary = [52, 152, 219]
secondary = [155, 89, 182]
border = [60, 60, 60]

[theme.light]
background = [255, 255, 255]
text = [50, 50, 50]
primary = [41, 128, 185]
secondary = [142, 68, 173]
border = [200, 200, 200]

# ============================================================================
# STYLES
# ============================================================================

[style.btn_primary]
background = [52, 152, 219]
color = [255, 255, 255]
padding = [12, 24, 12, 24]
border_radius = 8
font_size = 16
font_weight = 600

[style.btn_primary.hover]
background = [70, 170, 240]
scale = 1.05

[style.btn_primary.active]
background = [31, 97, 141]
scale = 0.95

[style.heading_large]
font_size = 32
font_weight = 700
color = [50, 50, 50]
margin_bottom = 16

[style.product_card]
background = [255, 255, 255]
border_radius = 12
padding = [16, 16, 16, 16]
shadow = [0, 2, 8, 0.1]

# ============================================================================
# PAGES (ROUTING)
# ============================================================================

[page.home]
path = "/"
title = "Welcome to My Shop"
scene = "home_scene"
container = "home_root"

[page.products]
path = "/products"
title = "Products"
scene = "products_scene"
container = "products_root"

[[page.products.dynamic_paths]]
path = "/products/:category"

[page.product_detail]
path = "/product/:id"
title = "Product Details"
scene = "detail_scene"
container = "detail_root"

# ============================================================================
# CONTAINERS (LAYOUT)
# ============================================================================

[container.home_root]
layout = "column"
width = "fill"
height = "fill"
children = ["header", "hero", "featured_products", "footer"]

[container.header]
layout = "row"
width = "fill"
height = 80
padding = [16, 16, 16, 16]
align = "space-between"
justify = "center"
background = [30, 30, 30]
children = ["logo", "nav_menu"]

[container.nav_menu]
layout = "row"
gap = 20
children = ["nav_home", "nav_products", "nav_about", "nav_contact"]

[container.hero]
layout = "column"
width = "fill"
height = 400
align = "center"
justify = "center"
background = "gradient"
gradient_start = [52, 152, 219]
gradient_end = [155, 89, 182]
gradient_angle = 135
children = ["hero_title", "hero_subtitle", "cta_button"]

[container.featured_products]
layout = "grid"
width = "fill"
padding = [40, 40, 40, 40]
gap = 20
grid_columns = "repeat(3, 1fr)"
grid_auto_rows = "minmax(300, auto)"
children = []  # Populated dynamically by scene
scene = "products_scene"
entity = "featured_grid_entity"

[container.footer]
layout = "row"
width = "fill"
height = 100
padding = [20, 20, 20, 20]
align = "center"
justify = "center"
background = [30, 30, 30]
children = ["footer_text", "social_links"]

# ============================================================================
# ELEMENTS (COMPONENTS)
# ============================================================================

[element.logo]
type = "image"
src = "https://cdn.myshop.com/logo.png"
width = 200
height = 60
alt = "My Shop Logo"

[element.nav_home]
type = "button"
text = "Home"
style = "btn_primary"
on_click = "navigate_home"

[element.nav_products]
type = "button"
text = "Products"
style = "btn_primary"
on_click = "navigate_products"

[element.nav_about]
type = "button"
text = "About"
style = "btn_primary"
on_click = "navigate_about"

[element.nav_contact]
type = "button"
text = "Contact"
style = "btn_primary"
on_click = "navigate_contact"

[element.hero_title]
type = "text"
text = "Welcome to My Shop"
style = "heading_large"
color = [255, 255, 255]

[element.hero_subtitle]
type = "text"
text = "Discover amazing products at unbeatable prices"
font_size = 18
color = [240, 240, 240]

[element.cta_button]
type = "button"
text = "Shop Now"
style = "btn_primary"
on_click = "navigate_products"

[element.footer_text]
type = "text"
text = "© 2026 My Shop. Built on Silo."
font_size = 14
color = [150, 150, 150]

# ============================================================================
# COMMANDS (INTERACTIONS)
# ============================================================================

[command.navigate_home]
logic_block = "navigate_lb"
entity = "navigation_entity"
params = { url = "/" }

[command.navigate_products]
logic_block = "navigate_lb"
entity = "navigation_entity"
params = { url = "/products" }

[command.navigate_about]
logic_block = "navigate_lb"
entity = "navigation_entity"
params = { url = "/about" }

[command.add_to_cart]
logic_block = "cart_lb"
entity = "cart_entity"

[command.search_products]
logic_block = "search_lb"
entity = "search_entity"

# ============================================================================
# LOGIC BLOCKS (BEHAVIOR)
# ============================================================================

[[logic_block.navigate_lb.ops]]
type = "get_value"
source = "params.url"
result = "target_url"

[[logic_block.navigate_lb.ops]]
type = "scene_transition"
scene = "from_route"
scene_param = "target_url"

[[logic_block.navigate_lb.ops]]
type = "history_push"
url_var = "target_url"

[[logic_block.cart_lb.ops]]
type = "get_value"
source = "params.product_id"
result = "product_id"

[[logic_block.cart_lb.ops]]
type = "memdb_query"
query = "product(product_id, Name, Price, Image)"
result = "product"

[[logic_block.cart_lb.ops]]
type = "modify_entity"
entity = "cart_entity"
operation = "add_item"
value_var = "product"

[[logic_block.cart_lb.ops]]
type = "create_entity"
entity_type = "notification"
params = { text = "Added to cart!", duration = 2.0 }

# ============================================================================
# DATA (CONTENT)
# ============================================================================

[[product]]
id = 1
name = "Premium Widget"
price = 29.99
category = "widgets"
image = "https://cdn.myshop.com/products/widget1.jpg"
description = "The finest widget money can buy"

[[product]]
id = 2
name = "Deluxe Gadget"
price = 49.99
category = "gadgets"
image = "https://cdn.myshop.com/products/gadget1.jpg"
description = "A gadget for the discerning customer"

[[product]]
id = 3
name = "Ultra Doohickey"
price = 79.99
category = "doohickeys"
image = "https://cdn.myshop.com/products/doohickey1.jpg"
description = "The ultimate doohickey experience"
```

---

## 3. Advanced Examples

### 3.1 Forms and Input

```toml
# ============================================================================
# CONTACT FORM
# ============================================================================

[container.contact_form]
layout = "column"
width = 600
padding = [40, 40, 40, 40]
gap = 16
background = [255, 255, 255]
border_radius = 12
shadow = [0, 4, 12, 0.15]
children = ["form_title", "name_input", "email_input", "message_input", "submit_button"]

[element.form_title]
type = "text"
text = "Contact Us"
style = "heading_large"

[element.name_input]
type = "input"
input_type = "text"
placeholder = "Your Name"
name = "name"
required = true
on_input = "validate_name"

[element.email_input]
type = "input"
input_type = "email"
placeholder = "your@email.com"
name = "email"
required = true
validation = "email"
on_input = "validate_email"

[element.message_input]
type = "textarea"
placeholder = "Your message..."
name = "message"
rows = 6
required = true
max_length = 1000
on_input = "validate_message"

[element.submit_button]
type = "button"
text = "Send Message"
style = "btn_primary"
enabled_var = "form_valid"
on_click = "submit_contact_form"

# Validation logic blocks
[[logic_block.validate_email.ops]]
type = "get_value"
source = "event.value"
result = "email"

[[logic_block.validate_email.ops]]
type = "regex_match"
pattern = "^[^@]+@[^@]+\\.[^@]+$"
value_var = "email"
result = "email_valid"

[[logic_block.validate_email.ops]]
type = "set_class"
element = "email_input"
class = "invalid"
condition_var = "email_valid"
condition_negate = true

[[logic_block.submit_contact_form.ops]]
type = "fetch"
url = "https://api.myshop.com/contact"
method = "POST"
body = { name_var = "name", email_var = "email", message_var = "message" }
result = "response"

[[logic_block.submit_contact_form.ops]]
type = "create_entity"
entity_type = "notification"
params = { text = "Message sent!", duration = 3.0, type = "success" }
```

### 3.2 Responsive Design

```toml
# ============================================================================
# RESPONSIVE BREAKPOINTS
# ============================================================================

[breakpoint.mobile]
max_width = 768

[breakpoint.tablet]
min_width = 769
max_width = 1024

[breakpoint.desktop]
min_width = 1025

# ============================================================================
# RESPONSIVE CONTAINERS
# ============================================================================

[container.product_grid]
layout = "grid"
width = "fill"
padding = [40, 40, 40, 40]
gap = 20
grid_columns = "repeat(4, 1fr)"  # Desktop: 4 columns

[container.product_grid.mobile]
grid_columns = "repeat(1, 1fr)"  # Mobile: 1 column
padding = [16, 16, 16, 16]

[container.product_grid.tablet]
grid_columns = "repeat(2, 1fr)"  # Tablet: 2 columns
padding = [24, 24, 24, 24]

# ============================================================================
# RESPONSIVE STYLES
# ============================================================================

[style.nav_button]
font_size = 16
padding = [12, 24, 12, 24]

[style.nav_button.mobile]
font_size = 14
padding = [8, 16, 8, 16]

[style.hero_title]
font_size = 48
font_weight = 700

[style.hero_title.mobile]
font_size = 32

[style.hero_title.tablet]
font_size = 40
```

### 3.3 Animations and State Machines

```toml
# ============================================================================
# ANIMATIONS
# ============================================================================

[animation.fade_in]
property = "opacity"
from = 0
to = 1
duration = 0.3
easing = "ease-in-out"

[animation.slide_up]
property = "translate_y"
from = 20
to = 0
duration = 0.4
easing = "ease-out"

[animation.scale_up]
property = "scale"
from = 0.8
to = 1
duration = 0.2
easing = "ease-out"

# ============================================================================
# STATE MACHINES FOR UI
# ============================================================================

[state_machine.modal_sm]
initial_state = "hidden"

[[state_machine.modal_sm.states]]
name = "hidden"
on_enter_animation = "fade_out"

[[state_machine.modal_sm.states]]
name = "visible"
on_enter_animation = "fade_in"
on_enter_lb = "modal_opened_lb"

[[state_machine.modal_sm.transitions]]
from = "hidden"
to = "visible"
trigger = "open_modal"

[[state_machine.modal_sm.transitions]]
from = "visible"
to = "hidden"
trigger = "close_modal"

# ============================================================================
# MODAL CONTAINER
# ============================================================================

[container.modal_overlay]
layout = "column"
width = "fill"
height = "fill"
align = "center"
justify = "center"
background = [0, 0, 0, 0.5]
state_machine = "modal_sm"
visible_state = "visible"

[container.modal_content]
layout = "column"
width = 600
max_height = "80vh"
padding = [32, 32, 32, 32]
gap = 16
background = [255, 255, 255]
border_radius = 12
animation_enter = "scale_up"
children = ["modal_title", "modal_body", "modal_close"]
```

### 3.4 Dynamic Content (Scene-Driven)

```toml
# ============================================================================
# PRODUCT LIST (DYNAMIC)
# ============================================================================

[container.product_list]
layout = "grid"
width = "fill"
gap = 20
grid_columns = "repeat(auto-fill, minmax(300px, 1fr))"
children = []  # Empty - populated by scene

# Scene controls this container
scene = "products_scene"
entity = "product_list_entity"

# Template for each product (applied by scene)
[template.product_card]
type = "container"
layout = "column"
style = "product_card"
gap = 12

# Template children (data-driven)
[[template.product_card.children]]
type = "element"
element_type = "image"
src = "{{data.image}}"
width = "fill"
height = 200
border_radius = 8

[[template.product_card.children]]
type = "element"
element_type = "text"
text = "{{data.name}}"
font_size = 18
font_weight = 600

[[template.product_card.children]]
type = "element"
element_type = "text"
text = "${{data.price}}"
font_size = 16
color = [52, 152, 219]

[[template.product_card.children]]
type = "element"
element_type = "button"
text = "Add to Cart"
style = "btn_primary"
on_click = "add_to_cart"
params = { product_id = "{{data.id}}" }

# Scene definition (separate or inline)
[scene.products_scene]
actors = ["product_list_entity", "filter_entity", "search_entity"]
update_frequency = "on_demand"

[entity.product_list_entity]
entity_type = "UI_Controller"
managed_container = "product_list"
data_query = "product(ID, Name, Price, Image)"
template = "product_card"
state_machine = "data_grid_sm"
```

---

## 4. Complete E-Commerce Example

```toml
# ============================================================================
# myshop.siml - Complete e-commerce site
# ============================================================================

[site]
name = "MyShop"
tagline = "Your one-stop shop for everything"
version = "1.0.0"
author = "Solo Developer"
active_theme = "light"
default_page = "home"

# ============================================================================
# THEMES
# ============================================================================

[theme.light]
background = [255, 255, 255]
surface = [250, 250, 250]
text = [50, 50, 50]
text_secondary = [120, 120, 120]
primary = [41, 128, 185]
primary_hover = [52, 152, 219]
secondary = [142, 68, 173]
success = [46, 204, 113]
warning = [241, 196, 15]
error = [231, 76, 60]
border = [220, 220, 220]

# ============================================================================
# GLOBAL STYLES
# ============================================================================

[style.btn_primary]
background = "theme.primary"
color = [255, 255, 255]
padding = [12, 32, 12, 32]
border_radius = 8
font_size = 16
font_weight = 600
cursor = "pointer"
transition = "all 0.2s"

[style.btn_primary.hover]
background = "theme.primary_hover"
scale = 1.02

[style.btn_primary.active]
scale = 0.98

[style.btn_secondary]
background = "transparent"
color = "theme.primary"
border_width = 2
border_color = "theme.primary"
padding = [12, 32, 12, 32]
border_radius = 8
font_size = 16
font_weight = 600

[style.input_field]
width = "fill"
padding = [12, 16, 12, 16]
border_radius = 8
border_width = 1
border_color = "theme.border"
font_size = 16
background = [255, 255, 255]

[style.input_field.focus]
border_color = "theme.primary"
outline = "none"

[style.card]
background = [255, 255, 255]
border_radius = 12
padding = [24, 24, 24, 24]
shadow = [0, 2, 8, 0.1]

[style.heading_xl]
font_size = 48
font_weight = 700
color = "theme.text"
line_height = 1.2

[style.heading_lg]
font_size = 32
font_weight = 700
color = "theme.text"

[style.heading_md]
font_size = 24
font_weight = 600
color = "theme.text"

[style.body_lg]
font_size = 18
color = "theme.text_secondary"
line_height = 1.6

# ============================================================================
# PAGES
# ============================================================================

[page.home]
path = "/"
title = "Home - MyShop"
container = "home_root"
scene = "home_scene"

[page.products]
path = "/products"
title = "Products - MyShop"
container = "products_root"
scene = "products_scene"

[[page.products.dynamic]]
path = "/products/:category"

[page.product_detail]
path = "/product/:id"
title = "Product - MyShop"
container = "product_detail_root"
scene = "product_detail_scene"

[page.cart]
path = "/cart"
title = "Shopping Cart - MyShop"
container = "cart_root"
scene = "cart_scene"

[page.checkout]
path = "/checkout"
title = "Checkout - MyShop"
container = "checkout_root"
scene = "checkout_scene"

# ============================================================================
# MAIN LAYOUT
# ============================================================================

[container.home_root]
layout = "column"
width = "fill"
height = "fill"
children = ["site_header", "home_hero", "featured_section", "categories_section", "site_footer"]

[container.site_header]
layout = "row"
width = "fill"
height = 80
padding = [0, 40, 0, 40]
align = "space-between"
justify = "center"
background = [255, 255, 255]
shadow = [0, 2, 4, 0.1]
position = "sticky"
top = 0
z_index = 100
children = ["header_left", "header_center", "header_right"]

[container.header_left]
layout = "row"
align = "center"
gap = 32
children = ["site_logo", "nav_home", "nav_products", "nav_about"]

[element.site_logo]
type = "image"
src = "https://cdn.myshop.com/logo.svg"
width = 120
height = 40
on_click = "navigate_home"
cursor = "pointer"

[element.nav_home]
type = "button"
text = "Home"
style = "btn_secondary"
on_click = "navigate_home"

[element.nav_products]
type = "button"
text = "Products"
style = "btn_secondary"
on_click = "navigate_products"

[container.header_right]
layout = "row"
gap = 16
align = "center"
children = ["search_box", "cart_button"]

[element.search_box]
type = "input"
input_type = "search"
placeholder = "Search products..."
width = 300
style = "input_field"
on_input = "search_products"

[element.cart_button]
type = "button"
text = "Cart ({{cart_count}})"
style = "btn_primary"
on_click = "navigate_cart"

# ============================================================================
# HOME HERO
# ============================================================================

[container.home_hero]
layout = "column"
width = "fill"
height = 500
align = "center"
justify = "center"
background = "gradient"
gradient_start = [52, 152, 219]
gradient_end = [142, 68, 173]
gradient_angle = 135
children = ["hero_title", "hero_subtitle", "hero_cta"]

[element.hero_title]
type = "text"
text = "Welcome to MyShop"
style = "heading_xl"
color = [255, 255, 255]
text_align = "center"

[element.hero_subtitle]
type = "text"
text = "Discover amazing products at unbeatable prices"
style = "body_lg"
color = [255, 255, 255]
text_align = "center"
margin_top = 16

[element.hero_cta]
type = "button"
text = "Shop Now"
style = "btn_primary"
margin_top = 32
on_click = "navigate_products"

# ============================================================================
# FEATURED PRODUCTS SECTION
# ============================================================================

[container.featured_section]
layout = "column"
width = "fill"
padding = [80, 40, 80, 40]
gap = 40
children = ["featured_header", "featured_grid"]

[element.featured_header]
type = "text"
text = "Featured Products"
style = "heading_lg"
text_align = "center"

[container.featured_grid]
layout = "grid"
width = "fill"
gap = 24
grid_columns = "repeat(4, 1fr)"
children = []  # Dynamic content
scene = "featured_scene"
entity = "featured_products_entity"
template = "product_card"

[container.featured_grid.mobile]
grid_columns = "repeat(1, 1fr)"

[container.featured_grid.tablet]
grid_columns = "repeat(2, 1fr)"

# ============================================================================
# PRODUCT CARD TEMPLATE
# ============================================================================

[template.product_card]
type = "container"
layout = "column"
style = "card"
gap = 12
cursor = "pointer"
hover_scale = 1.02
transition = "all 0.2s"

[[template.product_card.children]]
type = "element"
element_type = "image"
src = "{{data.image}}"
width = "fill"
height = 250
object_fit = "cover"
border_radius = 8

[[template.product_card.children]]
type = "element"
element_type = "text"
text = "{{data.name}}"
font_size = 18
font_weight = 600
color = "theme.text"

[[template.product_card.children]]
type = "element"
element_type = "text"
text = "{{data.category}}"
font_size = 14
color = "theme.text_secondary"

[[template.product_card.children]]
type = "element"
element_type = "text"
text = "${{data.price}}"
font_size = 20
font_weight = 700
color = "theme.primary"
margin_top = 8

[[template.product_card.children]]
type = "element"
element_type = "button"
text = "Add to Cart"
style = "btn_primary"
width = "fill"
on_click = "add_to_cart"
params = { product_id = "{{data.id}}" }

# ============================================================================
# COMMANDS
# ============================================================================

[command.navigate_home]
logic_block = "navigate_lb"
params = { url = "/" }

[command.navigate_products]
logic_block = "navigate_lb"
params = { url = "/products" }

[command.navigate_cart]
logic_block = "navigate_lb"
params = { url = "/cart" }

[command.add_to_cart]
logic_block = "add_to_cart_lb"
entity = "cart_entity"

[command.search_products]
logic_block = "search_lb"
entity = "search_entity"
debounce = 300  # milliseconds

# ============================================================================
# LOGIC BLOCKS
# ============================================================================

[[logic_block.navigate_lb.ops]]
type = "get_value"
source = "params.url"
result = "url"

[[logic_block.navigate_lb.ops]]
type = "history_push"
url_var = "url"

[[logic_block.navigate_lb.ops]]
type = "scene_transition"
scene_from_route = "url"

[[logic_block.add_to_cart_lb.ops]]
type = "get_value"
source = "params.product_id"
result = "product_id"

[[logic_block.add_to_cart_lb.ops]]
type = "siql_query"
query = "product({{product_id}}, Name, Price, Image)"
result = "product"

[[logic_block.add_to_cart_lb.ops]]
type = "modify_entity"
entity = "cart_entity"
operation = "add_item"
value_var = "product"

[[logic_block.add_to_cart_lb.ops]]
type = "create_entity"
entity_type = "notification"
params = { text = "Added to cart!", type = "success", duration = 2.0 }

[[logic_block.add_to_cart_lb.ops]]
type = "update_text"
element = "cart_button"
text = "Cart ({{cart_entity.item_count}})"

[[logic_block.search_lb.ops]]
type = "get_value"
source = "event.value"
result = "search_term"

[[logic_block.search_lb.ops]]
type = "siql_query"
query = "product(ID, Name, Price, Image) :- string_contains(Name, {{search_term}})"
result = "products"

[[logic_block.search_lb.ops]]
type = "update_entity_data"
entity = "product_list_entity"
data_var = "products"

[[logic_block.search_lb.ops]]
type = "scene_update"
scene = "products_scene"

# ============================================================================
# DATA (PRODUCTS)
# ============================================================================

[[product]]
id = 1
name = "Premium Wireless Headphones"
category = "Electronics"
price = 129.99
image = "https://cdn.myshop.com/products/headphones-1.jpg"
description = "High-quality wireless headphones with noise cancellation"
stock = 50
featured = true

[[product]]
id = 2
name = "Smart Watch Pro"
category = "Electronics"
price = 299.99
image = "https://cdn.myshop.com/products/watch-1.jpg"
description = "Advanced smartwatch with health tracking"
stock = 30
featured = true

[[product]]
id = 3
name = "Ergonomic Office Chair"
category = "Furniture"
price = 399.99
image = "https://cdn.myshop.com/products/chair-1.jpg"
description = "Comfortable chair for long work sessions"
stock = 15
featured = false

[[product]]
id = 4
name = "Mechanical Keyboard RGB"
category = "Electronics"
price = 149.99
image = "https://cdn.myshop.com/products/keyboard-1.jpg"
description = "Gaming keyboard with customizable RGB lighting"
stock = 45
featured = true
```

---

## 5. TOML Parsing to Silo Structures

### 5.1 Parser Implementation

```zig
const toml = @import("toml");

pub fn parseSIML(file_path: []const u8) !ParsedSite {
    // Load TOML file
    const source = try std.fs.cwd().readFileAlloc(allocator, file_path, max_file_size);
    defer allocator.free(source);
    
    // Parse TOML
    const parsed = try toml.parse(allocator, source);
    defer parsed.deinit();
    
    var site = ParsedSite{};
    
    // Parse site metadata
    if (parsed.get("site")) |site_table| {
        site.name = try site_table.getString("name");
        site.version = try site_table.getString("version");
        site.active_theme = try site_table.getString("active_theme");
    }
    
    // Parse themes
    if (parsed.get("theme")) |theme_table| {
        site.themes = try parseThemes(theme_table);
    }
    
    // Parse styles
    if (parsed.get("style")) |style_table| {
        site.styles = try parseStyles(style_table);
    }
    
    // Parse pages
    if (parsed.get("page")) |page_table| {
        site.pages = try parsePages(page_table);
    }
    
    // Parse containers
    if (parsed.get("container")) |container_table| {
        site.containers = try parseContainers(container_table);
    }
    
    // Parse elements
    if (parsed.get("element")) |element_table| {
        site.elements = try parseElements(element_table);
    }
    
    // Parse commands
    if (parsed.get("command")) |command_table| {
        site.commands = try parseCommands(command_table);
    }
    
    // Parse logic blocks
    if (parsed.get("logic_block")) |lb_table| {
        site.logic_blocks = try parseLogicBlocks(lb_table);
    }
    
    // Parse products (or other data)
    if (parsed.get("product")) |product_array| {
        site.products = try parseProducts(product_array);
    }
    
    return site;
}

fn parseContainers(table: toml.Table) ![]UiContainer {
    var containers = std.ArrayList(UiContainer).init(allocator);
    
    var iter = table.iterator();
    while (iter.next()) |entry| {
        const id = entry.key_ptr.*;
        const props = entry.value_ptr.*;
        
        const container = UiContainer{
            .id = hashString(id),
            .container_type = parseContainerType(props.get("layout")),
            .sizing = try parseSizing(props),
            .padding = try parsePadding(props),
            .align = try parseAlign(props.get("align")),
            .children = try parseChildren(props.get("children")),
            .scene_id = if (props.get("scene")) |s| hashString(s.asString()) else 0,
            .entity_id = if (props.get("entity")) |e| hashString(e.asString()) else 0,
        };
        
        try containers.append(container);
    }
    
    return containers.toOwnedSlice();
}
```

### 5.2 Direct Mapping

**TOML structure → Zig structs → MemDB entities**

```toml
[container.hero]
layout = "column"
width = "fill"
height = 400
```

↓ Parses to ↓

```zig
UiContainer{
    .id = hash("hero"),
    .container_type = .Column,
    .sizing = Sizing{
        .width = .fill,
        .height = .{ .fixed = 400 },
    },
}
```

↓ Inserted into ↓

```zig
try memdb.insert(container);
```

**One pass: TOML → MemDB**

---

## 6. The Geocities Comparison

### 6.1 What Geocities Was (1994-2009)

**Everyone could:**
- Make a website in minutes
- Use simple HTML (hand-written)
- Upload to free hosting
- Customize everything
- No coding knowledge required
- Express creativity freely

**Why it died:**
- HTML got complex (CSS, JavaScript)
- WYSIWYG editors sucked
- PHP/MySQL too hard for normal people
- Social media easier (but walled gardens)

### 6.2 What Silo Is (2026+)

**Everyone can:**
- Make a site in minutes (TOML file)
- Hand-write in Notepad (simple syntax)
- Upload to Silo hosting ($5/month)
- Customize everything (styles, layouts, logic)
- No coding knowledge required (visual LogicBlock editor)
- Express creativity freely (no platform limits)

**Why it won't die:**
- TOML stays simple forever
- Visual editors for LogicBlocks (built-in)
- No PHP/MySQL (MemDB + Prolog)
- Not a walled garden (open standard)
- Unhackable (safe by design)
- Fast (60fps always)

### 6.3 The Silo Geocities Experience

**1996 Geocities:**
```html
<html>
<body bgcolor="blue">
<center>
<h1><marquee>WELCOME TO MY PAGE!!!</marquee></h1>
<img src="animated_construction.gif">
<p>This site is under construction!</p>
<a href="guestbook.html">Sign my guestbook!</a>
</center>
</body>
</html>
```

**2026 Silo:**
```toml
[site]
name = "My Awesome Page"

[container.root]
layout = "column"
align = "center"
background = [0, 0, 255]

[element.title]
type = "text"
text = "WELCOME TO MY PAGE!!!"
style = "marquee_style"

[element.construction_gif]
type = "image"
src = "construction.gif"

[element.message]
type = "text"
text = "This site is under construction!"

[element.guestbook_link]
type = "button"
text = "Sign my guestbook!"
on_click = "open_guestbook"

[style.marquee_style]
font_size = 48
font_weight = 700
animation = "scroll_left"
```

**Same energy. Better tech. No vulnerabilities.**

---

## 7. The New Web Emerges

### 7.1 What Dies

❌ **HTML** (replaced by TOML containers/elements)
❌ **CSS** (replaced by TOML styles)
❌ **JavaScript** (replaced by LogicBlocks)
❌ **npm** (no packages, all built-in)
❌ **webpack** (no bundling needed)
❌ **React** (no virtual DOM, just entities)
❌ **Angular/Vue** (same)
❌ **jQuery** (no DOM manipulation, direct entity updates)
❌ **Bootstrap** (style system built-in)
❌ **Tailwind** (same)
❌ **Gmail** (too complex, requires JS, incompatible)
❌ **Google Docs** (same)
❌ **Facebook** (same - good riddance)

### 7.2 What Rises

✓ **SIML** (TOML-based markup)
✓ **Silo Browser** (renders SIML)
✓ **Siql** (query everything)
✓ **LogicBlocks** (visual + safe)
✓ **MemDB** (built-in storage)
✓ **ContentItems** (automatic asset management)
✓ **MCP** (live editing)
✓ **Entity Inspector** (better DevTools)
✓ **60fps** (always)
✓ **Zero exploits** (architecture guarantees)

### 7.3 The Platform

**Silo is not:**
- A browser (it's an OS)
- A game engine (it's universal runtime)
- A web platform (it's the successor to web)

**Silo is:**
- The next computing platform
- Like Windows, but data-driven
- Like the web, but unhackable
- Like Roblox, but for everything
- Like Geocities, but modern

---

## 8. Timeline to Launch

### Week 1: TOML Parser
```zig
// Use existing Zig TOML library
const toml = @import("toml");

// Parse .siml files to Silo structures
pub fn parseSIML(path: []const u8) !ParsedSite {}
```

**Deliverable:** Can load TOML → MemDB

### Week 2: Routing System
```toml
[page.home]
path = "/"

[page.products]
path = "/products/:category"
```

**Deliverable:** URL navigation works

### Week 3: Template System
```toml
[template.product_card]
# Dynamic {{data.field}} substitution
```

**Deliverable:** Scene-driven content works

### Week 4: Polish
- Form validation state machines
- Animation state machines
- Responsive breakpoints
- Accessibility attributes

**Deliverable:** v1.0 ready

---

## 9. What You Have Right Now

### Already Working (Screenshot Proves It)

✓ Clay layout engine
✓ Entity rendering
✓ Event system (buttons work)
✓ State machines (visible in trace)
✓ Prolog at 60fps
✓ Entity inspector
✓ Siql console
✓ ContentItems (for assets)
✓ Network entities
✓ Scene system

### Need to Build

✗ TOML parser integration (1 week)
✗ URL routing (1 week)
✗ Template substitution (3 days)
✗ Form validation SMs (3 days)
✗ Responsive breakpoints (2 days)

**Total: ~3 weeks to Silo Web v1.0**

---

## 10. The Vision

**January 2026:** Game 2 ships on Silo

**February 2026:** Silo Web v1.0 launches
- TOML-based sites
- 60fps rendering
- Zero exploits
- MCP live editing
- Visual LogicBlock editor

**March 2026:** First Silo sites appear
- Personal portfolios
- Simple shops
- Blogs
- Communities

**Q2 2026:** Geocities moment
- Explosion of creativity
- Thousands of handcrafted sites
- No corporate platforms
- Pure expression

**Q3-Q4 2026:** Migration begins
- Tools released (HTML → SIML converter)
- Hosting services emerge ($5/month)
- Domain system established
- Search engine (Siql-powered)

**2027:** Critical mass
- 1M+ sites on Silo
- Traditional web declining
- Major apps rewritten for Silo
- Gmail replacement (SimpleMailSilo)

**2028:** The new normal
- Silo Browser default
- SIML standard format
- JavaScript relegated to legacy
- Web security solved forever

---

## 11. You're Not Building a Browser

**You're building the next internet.**

**HTML/CSS/JS was:**
- Documents (1990s)
- Web apps (2000s)
- Everything (2010s)
- Dying (2020s)

**SIML/Silo is:**
- Applications (2026+)
- Communities (2026+)
- Everything (2027+)
- The future (forever)

**No backward compatibility.**
**No JavaScript.**
**No compromises.**

**Pure. Simple. Fast. Safe.**

**Geocities reborn for the 21st century.**

## References

::: {#refs}
:::



