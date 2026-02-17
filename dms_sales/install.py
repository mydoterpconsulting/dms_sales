import frappe
import os
import json

def after_install():
    """Auto-import workspaces and hide standard ERPNext workspaces"""
    
    # Step 1: Import DMS workspaces
    import_dms_workspaces()
    
    # Step 2: Hide standard ERPNext workspaces
    hide_standard_workspaces()

def import_dms_workspaces():
    """Import DMS Sales workspaces from JSON files"""
    
    workspace_dir = frappe.get_app_path("dms_sales", "mydot_dms_sales", "workspace")
    
    if not os.path.exists(workspace_dir):
        return
    
    workspaces_to_import = []
    
    # Find all workspace JSON files
    for root, dirs, files in os.walk(workspace_dir):
        for workspace_name in dirs:
            workspace_file = os.path.join(root, workspace_name, f"{workspace_name}.json")
            if os.path.exists(workspace_file):
                workspaces_to_import.append((workspace_name, workspace_file))
    
    # Import each workspace
    for workspace_name, workspace_file in workspaces_to_import:
        try:
            with open(workspace_file, "r") as f:
                workspace_data = json.load(f)
            
            # Check if workspace already exists
            if frappe.db.exists("Workspace", workspace_name):
                print(f"Workspace {workspace_name} already exists, skipping...")
                continue
            
            # Remove child tables that reference missing resources
            if "charts" in workspace_data:
                workspace_data["charts"] = []
            if "shortcuts" in workspace_data:
                # Keep shortcuts but filter out problematic ones
                workspace_data["shortcuts"] = [
                    s for s in workspace_data.get("shortcuts", []) 
                    if not s.get("link_to", "").startswith("Floor Stock")
                ]
            if "custom_blocks" in workspace_data:
                workspace_data["custom_blocks"] = []
            
            # Create workspace
            workspace_doc = frappe.get_doc(workspace_data)
            workspace_doc.flags.ignore_mandatory = True
            workspace_doc.flags.ignore_links = True
            workspace_doc.insert(ignore_permissions=True, ignore_mandatory=True)
            
            print(f"✅ Imported workspace: {workspace_name}")
            
        except Exception as e:
            print(f"❌ Failed to import {workspace_name}: {str(e)}")
    
    frappe.db.commit()

def hide_standard_workspaces():
    """Hide all standard ERPNext workspaces, keep only DMS workspaces visible"""
    
    # DMS workspaces to keep visible
    dms_workspaces = ["sa", "SA Manager", "SA Admin", "HR DC Auto", "tutorial"]
    
    # Get all public workspaces that are NOT DMS workspaces
    workspaces_to_hide = frappe.get_all("Workspace", 
        filters={
            "public": 1,
            "name": ["not in", dms_workspaces]
        },
        pluck="name")
    
    if workspaces_to_hide:
        print(f"\n📦 Hiding {len(workspaces_to_hide)} standard ERPNext workspaces...")
        
        for workspace_name in workspaces_to_hide:
            frappe.db.set_value("Workspace", workspace_name, "public", 0)
        
        frappe.db.commit()
        print(f"✅ Hidden {len(workspaces_to_hide)} workspaces. Only DMS workspaces are visible.")
