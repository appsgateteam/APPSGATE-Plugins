# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Marcoms Customization',
    'summary': 'all Marcoms Customization',
    'depends': ['oh_employee_documents_expiry','om_account_asset','uom','account','acc_pi','crm','sales_team','hr_payroll','sale','sale_crm','base','hr','purchase','purchase_requisition'],
    'data': [
        'views/test_view.xml',
        'report/sale_report_templates.xml',
        'report/report_temp.xml',
        'report/report_templates.xml',
        'report/report_lead_form.xml',
        'report/payment_request.xml',
        'report/report_mar_quotation.xml',
        'report/report_pending_supporting_doc.xml',
        'report/report_invoice.xml',
        'report/report_invoice_new.xml',
        'report/purchase_order_templates.xml',
        'report/report_minimum_stock_level.xml',
        'report/report_payment_receipt_templates.xml',
        'report/report_payment_receipt_templates_new.xml',
        'report/report_journal_entries_view.xml',
        'report/report_invoice_templates.xml',
        'report/purchase_quotation_templates.xml',
        'report/report_stockpicking_operations.xml',
        'report/report_invoice_without_seal.xml',
        'report/report_check_base.xml',
        'report/report_check_base_journal.xml',
        'report/report_check_base_rak.xml',
        'report/report_check_base_rak_journal.xml',
        'report/report_deliveryslip.xml',
        'report/job_costing_report.xml',
        'security/ir.model.access.csv',
        'security/mar_security.xml',
        'wizard/add_qty.xml',
        'wizard/gen_po.xml',
        'wizard/job_costing.xml',
        'data/mail_data.xml',
        'data/crm_data.xml',
    ],
    'css': ['static/src/css/crmm.css'],
    'installable': True,
    'auto_install': False,
    'application': True,
}

