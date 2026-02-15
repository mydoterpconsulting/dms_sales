# Mydot DMS Sales

**Dealer Management System for Automotive Sales & Service**

Complete ERPNext solution for automotive dealerships managing vehicle sales, financing, commissions, and inventory. Built specifically for Malaysian Perodua dealerships with multi-bank integration.

## ✨ Features

### 📦 Complete Package
- **44 Custom DocTypes** - Full sales workflow coverage
- **64 Print Formats** - Professional bank forms and quotations (1.5 MB Jinja templates)
- **52 Custom Fields** - Extended ERPNext for dealership needs
- **4 Workflows** - Approval processes (VSO, Car Details, Stock Request, Commission)
- **2 Custom Reports** - Commission tracking and sales analysis
- **88 Master Data Records** - Auto-installed (states, insurance, car models, colors)

### 🚗 Sales Management
- **VSO (Vehicle Sales Order)** - Complete sales workflow from booking to delivery
- **Prospect Booking Form** - Lead capture with car preference tracking
- **Car Stock Request** - Inventory allocation system with workflow
- **Car Details & Checklist** - Pre-delivery inspection and documentation
- **ICO Fulfillment** - Inventory control and allocation

### 💰 Finance Integration
**6 Malaysian Banks** - Pre-built forms with auto-calculations:
- **PAR (Purchase & Retail Agreement)** - Main sales financing form
- **PBR CIMB** - CIMB Bank pre-booking request (8 pages)
- **PBR HLBB** - Hong Leong Bank pre-booking (8 pages)
- **PBR PBB** - Public Bank pre-booking (9 pages MERGE format)
- **Floor Stock Facilities** - AMBank, Maybank, RHB inventory financing

**Features:**
- Auto-calculation of totals, insurance, road tax
- Number-to-word conversion
- Insurance premium calculations
- Financing amount breakdowns

### 👥 Commission Management
- **SA Commission Claim Form** - Multi-level approval workflow
- **Commission Report** - Track earnings by sales advisor
- **SA Registered Month** - Sales performance by registration date
- **Commission Calculation** - Auto-calculate commissions (requires client script recreation)

### 📊 Inventory Management
- **Floor Stock Vehicle** - Track financed inventory (MBB, AMB, RHB)
- **Car Stock Request** - Allocation workflow with 27+ automation scripts
- **Car Model Variants** - Trim levels, colors, pricing
- **Car Model Colors** - Color codes and types (metallic, solid, two-tone)

### 🏦 Master Data (Auto-Installed)
- **16 Malaysian States** - Complete geographic coverage
- **6 Insurance Companies** - Allianz, Great Eastern, Pacific, Tokio Marine, Tune Protect, Zurich
- **8 Perodua Models** - Axia, Bezza, Myvi, Alza, Aruz, Ativa
- **6 Color Types** - Metallic, solid, special metallic, two-tone, R75

## 📋 Requirements

- **ERPNext v15.0.0 or higher** (tested on v15.65.4)
- **Frappe Framework v15+**
- **HRMS app** (for employee/sales advisor management)
- **Python 3.10+**
- **MariaDB 10.6+**

## 🚀 Installation

### Step 1: Get the App

```bash
cd /path/to/frappe-bench
bench get-app https://github.com/mydotconsulting/dms_sales.git
```

### Step 2: Install on Site

```bash
bench --site your-site.com install-app dms_sales
bench --site your-site.com migrate
bench build
bench restart
```

### Step 3: Verify Installation

Check that master data loaded:

```bash
bench --site your-site.com console
```

```python
>>> frappe.db.count("State")
16
>>> frappe.db.count("Insurance Company")
6
>>> frappe.db.count("Car Model")
8
>>> frappe.db.count("Car Color Type")
6
```

## ⚙️ First-Time Setup

### ✅ Auto-Installed (No Action Needed)

The following data is installed automatically via fixtures:

| Data Type | Count | What's Included |
|-----------|-------|-----------------|
| **States** | 16 | All Malaysian states + federal territories |
| **Insurance** | 6 | Major insurance providers |
| **Car Models** | 8 | Current Perodua lineup |
| **Color Types** | 6 | Industry-standard color classifications |
| **Custom Fields** | 52 | Workflow states, WooCommerce integration, HR fields |

**Total setup time:** < 5 minutes (just app installation)

### ⚠️ Manual Configuration Required (1-2 hours)

After installation, you need to configure:

#### 1. Sales Team Setup
Navigate to **Sales Advisor** DocType and add your team:
- Sales Advisor name
- Employee link (from HRMS)
- Commission rates
- Contact information

#### 2. Banking Contacts
Navigate to **Banker** DocType and add:
- Bank name (CIMB, HLBB, PBB, etc.)
- Banker contact person
- Email and phone

#### 3. Car Inventory
Navigate to **Car Model Variant** and add:
- Model (from pre-loaded Perodua models)
- Variant code (e.g., "1.5 AV", "1.3 G")
- Retail price
- Color options

Navigate to **Car Model Color** and add:
- Color name
- Color code (from manufacturer)
- Color type (from pre-loaded types)

#### 4. Print Format Branding
Customize print formats with your company logo:
- Go to **Print Settings**
- Upload company letterhead
- Configure print format header/footer

#### 5. User Roles
Assign roles to users:
- **Sales Advisor** - Create VSO, view own commissions
- **SA Manager** - Approve commission claims
- **SA Admin** - Full access to sales data
- **DC HR** - HR approvals, commission processing

## ⚠️ Known Limitations

### Client Scripts: 6% Exported (5 of 88)

**What Works:**
- ✅ Basic form functionality
- ✅ All DocTypes render correctly
- ✅ Workflows function
- ✅ Print formats available

**What's Missing (83 scripts need recreation):**
- ❌ **Auto-calculations** - Gear totals, insurance, subtotals, commissions
- ❌ **Dynamic filtering** - Filter variants by model, colors by variant
- ❌ **Auto-fill logic** - Engine/chassis numbers, date auto-population
- ❌ **Button actions** - Create PAR, PBL, checklist, FS request buttons
- ❌ **Validations** - Vehicle plate checks, tender number validation
- ❌ **UI customizations** - Hide sidebars, read-only fields by role

**Why:** 83 client scripts in the original sandbox have no module assigned (`module: null`), preventing standard export.

**Workarounds:**
1. **Recommended:** Recreate top 10 critical scripts (~10 hours for 90% functionality)
   - Priority: Commission calculations, VSO quotations, variant filtering, PAR button, engine/chassis autosave
2. **Database migration:** Export full sandbox database (includes all scripts)
3. **Fixture export:** Export client scripts as fixtures (advanced)

See `/root/marvin/content/dms-sales-client-scripts-export.md` for full details and script list.

## 📦 What's Included

### DocTypes (44 total)

**Sales Workflow (8 DocTypes):**
- VSO, Prospect Booking Form, Car Booking, Car Stock Request, Car Details And Checklist, ICO Fulfillment, Announcement, Sales Advisor

**Finance Forms (10 DocTypes):**
- PAR, PBR CIMB, PBR HLBB, PBR PBB, Floor Stock Facility Request AMB/MBB/RHB, Floor Stock Vehicle MBB, Banker

**Commission (2 DocTypes):**
- SA Commission Claim Form, SA Commission Disbursement

**Master Data (13 DocTypes):**
- Car Model, Car Model Variant, Car Model Color, Car Color Type, Insurance Company, State, Bank, Sales Target, Sales Organization, Branch, Dealership, Showroom, Workshop

**Inventory (4 DocTypes):**
- Car Stock Item, Stock Allocation, Stock Transfer, Stock Audit

**Others (7 DocTypes):**
- Customer Feedback, Test Drive, Trade In, Insurance Claim, Warranty Claim, Service Package, Loyalty Program

### Print Formats (64 total, 1.5 MB)

**Bank Forms (33 formats):**
- PAR - 7 formats (main, annexures, schedules)
- PBR CIMB - 8 formats (multi-page forms)
- PBR HLBB - 8 formats
- PBR PBB - 10 formats (including 104 KB MERGE format)

**Floor Stock (20 formats):**
- AMB - 4 formats
- MBB - 12 formats
- RHB - 4 formats

**Sales (11 formats):**
- VSO quotations, car checklists, stock requests

### Custom Fields (52 fields)

**Workflow States (4):**
- VSO, Car Details And Checklist, Car Stock Request, SA Commission Claim Form

**WooCommerce Integration (6):**
- Address, Customer, Item, Sales Order (woocommerce_id, woocommerce_email)

**HR & Payroll (31):**
- Company, Department, Designation, Employee (approvers, cost centers, insurance)

**Other (11):**
- Contact (billing contact), Print Settings, Project, Task, Terms and Conditions, Timesheet

### Reports (2)

1. **Commission Report** - Track SA earnings by claim form
2. **SA Registered Month** - Sales by registration date

## 🔄 Deployment

### Install on New Site

```bash
# 1. Install app
bench --site mysite.com install-app dms_sales

# 2. Migrate (imports fixtures)
bench --site mysite.com migrate

# 3. Verify fixtures loaded
bench --site mysite.com console
>>> frappe.db.count("State")
16
>>> frappe.db.count("Insurance Company")
6
>>> frappe.db.count("Car Model")
8
```

### Update Existing Site

```bash
# 1. Pull latest code
cd apps/dms_sales
git pull origin main

# 2. Migrate (imports new fixtures)
bench --site mysite.com migrate

# 3. Clear cache
bench --site mysite.com clear-cache

# 4. Restart
bench restart
```

## 🛠️ Development

### Prerequisites

- Python 3.10+
- Node.js 18+
- Frappe Bench installed

### Setup Development Environment

```bash
# Get the app
cd /path/to/frappe-bench
bench get-app https://github.com/mydotconsulting/dms_sales.git

# Install on dev site
bench --site dev.localhost install-app dms_sales

# Start development server
bench start
```

### Adding New Features

**Add new DocType:**
```bash
bench --site dev.localhost new-doctype "My DocType" --module "DMS Sales"
```

**Export customizations:**
```bash
bench --site dev.localhost export-doc "DocType" "My DocType" --module "DMS Sales"
```

**Update fixtures:**
Edit `/apps/dms_sales/dms_sales/hooks.py` and add to `fixtures` list.

### Contributing

This app uses `pre-commit` for code formatting:

```bash
cd apps/dms_sales
pre-commit install
```

Pre-commit tools:
- **ruff** - Python linting and formatting
- **eslint** - JavaScript linting
- **prettier** - Code formatting
- **pyupgrade** - Python syntax upgrades

## 📊 Statistics

### Export Summary

| Component | Count | Size | Status |
|-----------|-------|------|--------|
| **DocTypes** | 44 | - | ✅ 100% |
| **Workflows** | 4 | - | ✅ 100% |
| **Custom Fields** | 52 | 61 KB | ✅ 100% |
| **Print Formats** | 64 | 1.5 MB | ✅ 100% |
| **Reports** | 2 | 2.7 KB | ✅ 100% |
| **Client Scripts** | 5 | 52 KB | ⚠️ 6% |
| **Master Data** | 88 records | 84 KB | ✅ 100% |

**Total Exported:** 259 components
- **171 code components** (DocTypes, workflows, fields, formats, reports, scripts)
- **88 data records** (states, insurance, models, colors, custom fields)

### File Structure

```
dms_sales/
├── dms_sales/
│   ├── dms_sales/
│   │   ├── doctype/              # 44 DocTypes
│   │   ├── print_format/         # 64 Jinja templates (1.5 MB)
│   │   ├── report/               # 2 custom reports
│   │   ├── client_script/        # 5 exported scripts (52 KB)
│   │   └── workflow/             # 4 workflows
│   ├── fixtures/                 # Master data (88 records, 84 KB)
│   │   ├── state.json            # 16 Malaysian states
│   │   ├── insurance_company.json # 6 insurance providers
│   │   ├── car_model.json        # 8 Perodua models
│   │   └── car_color_type.json   # 6 color types
│   └── hooks.py                  # App configuration
├── README.md                     # This file
├── requirements.txt              # Python dependencies
└── package.json                  # Node dependencies
```

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Support

For issues, questions, or feature requests:
- **GitHub Issues:** https://github.com/mydotconsulting/dms_sales/issues
- **Email:** amirul.zulkefli@mydotconsulting.com
- **Documentation:** See `/root/marvin/content/` for detailed export notes

## 🎯 Roadmap

### Short-term
- [ ] Recreate top 10 critical client scripts for auto-calculations
- [ ] Add Proton car models alongside Perodua
- [ ] Export remaining 83 client scripts as fixtures

### Medium-term
- [ ] Dashboard widgets for sales performance
- [ ] Mobile app for sales advisors
- [ ] WhatsApp integration for customer notifications
- [ ] Advanced analytics and reporting

### Long-term
- [ ] Multi-brand support (Toyota, Honda, Mazda)
- [ ] Service department integration (DMS Service)
- [ ] CRM features (lead nurturing, follow-ups)
- [ ] E-commerce integration (online bookings)

---

**Built by Mydot Consulting** - Empowering Malaysian automotive dealerships with modern ERP solutions.

*Exported from sandbox-sales.mydotconsulting.com on 2026-02-15*
