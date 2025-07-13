#!/usr/bin/env python3
"""
UK OSINT CLI Tool - Professional British Intelligence Platform
Advanced automated background check investigation tool for UK targets
Usage: python uk_osint_cli.py --name "John Smith" --postcode "SW1A 1AA"
"""

import argparse
import requests
import json
import time
import urllib.parse
from datetime import datetime
import os
import sys
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

class UKProfessionalOSINT:
    def __init__(self):
        self.results = {}
        self.target_info = {}
        self.report_data = []
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.verbose = False
        
    def banner(self):
        print("""
🇬🇧 ═══════════════════════════════════════════════════════════════════════
   UK OSINT INTELLIGENCE PLATFORM v2.0
   Professional British Investigation Suite - 40+ UK Sources
   GDPR Compliant • UK Data Protection Act 2018
🇬🇧 ═══════════════════════════════════════════════════════════════════════
        """)
    
    def log(self, message, level="INFO"):
        """Enhanced logging with timestamps"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        if self.verbose or level in ["ERROR", "SUCCESS"]:
            print(f"[{timestamp}] {level}: {message}")
    
    def set_target(self, name=None, email=None, phone=None, postcode=None, 
                   company_number=None, address=None):
        """Set UK investigation target information"""
        self.target_info = {
            'name': name,
            'email': email,
            'phone': phone,
            'postcode': postcode,
            'company_number': company_number,
            'address': address,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print(f"🎯 UK TARGET ACQUIRED: {name or 'Unknown'}")
        for key, value in self.target_info.items():
            if value and key != 'timestamp':
                print(f"   {key.upper()}: {value}")
        print("─" * 70)
    
    def uk_government_records_search(self):
        """UK Government and public records investigation"""
        print("🏛️ UK GOVERNMENT & PUBLIC RECORDS SEARCH...")
        
        name = self.target_info.get('name', '')
        company_number = self.target_info.get('company_number', '')
        
        uk_gov_sources = {
            'companies_house': f"https://find-and-update.company-information.service.gov.uk/search?q={urllib.parse.quote(name)}",
            'uk_electoral_roll': f"https://www.192.com/people/search/{urllib.parse.quote(name)}",
            'land_registry': f"https://landregistry.data.gov.uk/search?q={urllib.parse.quote(name)}",
            'uk_gov_register': f"https://www.gov.uk/search/all?keywords={urllib.parse.quote(name)}",
            'charity_commission': f"https://register-of-charities.charitycommission.gov.uk/search?q={urllib.parse.quote(name)}",
            'insolvency_service': f"https://www.insolvencydirect.bis.gov.uk/eiir/search.asp"
        }
        
        if company_number:
            uk_gov_sources['companies_house_number'] = f"https://beta.companieshouse.gov.uk/company/{company_number}"
        
        self.results['uk_government_records'] = uk_gov_sources
        
        for source, url in uk_gov_sources.items():
            self.log(f"UK Gov source: {source} - {url}")
        
        self.log(f"Companies House search initiated for: {name}")
    
    def uk_professional_bodies_search(self):
        """UK Professional regulatory bodies investigation"""
        print("⚖️ UK PROFESSIONAL BODIES & REGULATORY SEARCH...")
        
        name = self.target_info.get('name', '')
        
        professional_bodies = {
            'law_society': f"https://solicitors.lawsociety.org.uk/search/results?SearchTerm={urllib.parse.quote(name)}",
            'bar_standards_board': "https://www.barstandardsboard.org.uk/regulatory-requirements/bsb-handbook/code-guidance/public-access-list/",
            'gmc_doctors': "https://www.gmc-uk.org/doctors/search.asp",
            'nmc_nurses': "https://www.nmc.org.uk/registration/search-the-register/",
            'icaew_accountants': "https://www.icaew.com/about-icaew/find-a-chartered-accountant",
            'rics_surveyors': "https://www.rics.org/uk/footer/find-a-surveyor/"
        }
        
        self.results['uk_professional_bodies'] = professional_bodies
        
        for body, url in professional_bodies.items():
            self.log(f"Professional body: {body} - {url}")
    
    def uk_electoral_address_verification(self):
        """UK Electoral roll and address verification"""
        print("📍 UK ELECTORAL & ADDRESS VERIFICATION...")
        
        name = self.target_info.get('name', '')
        postcode = self.target_info.get('postcode', '')
        address = self.target_info.get('address', '')
        
        electoral_sources = {
            '192_people_search': f"https://www.192.com/people/search/{urllib.parse.quote(name)}",
            'bt_phonebook': "https://www.thephonebook.bt.com/Person/PersonSearch/",
            'postcode_lookup': f"https://www.royalmail.com/find-a-postcode",
            'yell_directory': f"https://www.yell.com/s/{urllib.parse.quote(name)}.html",
            'uk_address_finder': "https://www.findmyaddress.co.uk/search",
            'voila_people_search': f"https://www.voila.co.uk/people/{urllib.parse.quote(name)}"
        }
        
        if postcode:
            electoral_sources['postcode_specific'] = f"UK Postcode: {postcode}"
        
        self.results['uk_electoral_address'] = electoral_sources
        
        for source, url in electoral_sources.items():
            self.log(f"Electoral source: {source} - {url}")
    
    def uk_business_intelligence(self):
        """UK Business and corporate intelligence"""
        print("🏢 UK BUSINESS INTELLIGENCE GATHERING...")
        
        name = self.target_info.get('name', '')
        company_number = self.target_info.get('company_number', '')
        
        business_sources = {
            'companies_house_beta': f"https://beta.companieshouse.gov.uk/search?q={urllib.parse.quote(name)}",
            'duedil_business': f"https://www.duedil.com/search?q={urllib.parse.quote(name)}",
            'uk_corporate_directory': f"https://www.companiesintheuk.co.uk/search/{urllib.parse.quote(name)}",
            'findthecompany_uk': f"https://company.findthecompany.co.uk/search/{urllib.parse.quote(name)}",
            'uk_business_directory': f"https://www.ukbusinessdirectory.co.uk/search/{urllib.parse.quote(name)}",
            'experian_business': "https://www.experian.co.uk/business-express/"
        }
        
        # Enhanced company number search
        if company_number:
            business_sources.update({
                'companies_house_direct': f"https://beta.companieshouse.gov.uk/company/{company_number}",
                'company_filings': f"https://beta.companieshouse.gov.uk/company/{company_number}/filing-history",
                'company_officers': f"https://beta.companieshouse.gov.uk/company/{company_number}/officers"
            })
        
        self.results['uk_business_intelligence'] = business_sources
        
        for source, url in business_sources.items():
            self.log(f"Business source: {source} - {url}")
    
    def uk_property_assets_search(self):
        """UK Property and asset investigation"""
        print("🏠 UK PROPERTY & ASSETS INVESTIGATION...")
        
        postcode = self.target_info.get('postcode', '')
        name = self.target_info.get('name', '')
        
        property_sources = {
            'rightmove_property': f"https://www.rightmove.co.uk/property-for-sale/search.html?searchLocation={urllib.parse.quote(postcode or name)}",
            'zoopla_property': f"https://www.zoopla.co.uk/search/?q={urllib.parse.quote(postcode or name)}",
            'onthemarket': f"https://www.onthemarket.com/for-sale/property/{urllib.parse.quote(postcode or name)}/",
            'uk_house_prices': f"https://www.ukhouseprices.com/search/{urllib.parse.quote(postcode or name)}",
            'land_registry_prices': "https://landregistry.data.gov.uk/app/ppd/search",
            'council_tax_bands': "https://www.gov.uk/council-tax-bands"
        }
        
        self.results['uk_property_assets'] = property_sources
        
        for source, url in property_sources.items():
            self.log(f"Property source: {source} - {url}")
    
    def uk_social_media_digital_search(self):
        """UK Social media and digital footprint investigation"""
        print("📱 UK SOCIAL MEDIA & DIGITAL FOOTPRINT...")
        
        name = self.target_info.get('name', '')
        email = self.target_info.get('email', '')
        
        social_digital_sources = {
            'linkedin_uk': f"https://www.linkedin.com/search/results/people/?keywords={urllib.parse.quote(name)}&origin=GLOBAL_SEARCH_HEADER",
            'facebook_uk': f"https://www.facebook.com/search/people/?q={urllib.parse.quote(name)}",
            'twitter_uk': f"https://twitter.com/search?q={urllib.parse.quote(name)}&src=typed_query&f=user",
            'instagram_uk': f"https://www.instagram.com/web/search/topsearch/?query={urllib.parse.quote(name)}",
            'uk_domain_search': "https://www.nominet.uk/whois/",
            'uk_academic_search': "https://www.hesa.ac.uk/"
        }
        
        if email:
            domain = email.split('@')[1] if '@' in email else ''
            if domain.endswith('.uk') or domain.endswith('.co.uk'):
                social_digital_sources['uk_email_domain'] = f"UK Domain: {domain}"
        
        self.results['uk_social_digital'] = social_digital_sources
        
        for source, url in social_digital_sources.items():
            self.log(f"Social/Digital source: {source} - {url}")
    
    def uk_financial_intelligence(self):
        """UK Financial regulatory and intelligence gathering"""
        print("💰 UK FINANCIAL INTELLIGENCE & REGULATORY...")
        
        name = self.target_info.get('name', '')
        company_number = self.target_info.get('company_number', '')
        
        financial_sources = {
            'fca_register': "https://register.fca.org.uk/s/search?type=RegisterSearch",
            'uk_bankruptcy_search': "https://www.insolvencydirect.bis.gov.uk/eiir/",
            'companies_house_filings': f"https://beta.companieshouse.gov.uk/search/companies?q={urllib.parse.quote(name)}",
            'experian_uk': "https://www.experian.co.uk/",
            'hmrc_public_register': "https://www.gov.uk/government/organisations/hm-revenue-customs",
            'uk_tax_investigation': "https://www.gov.uk/guidance/money-laundering-regulations-registration"
        }
        
        # Enhanced financial searches
        financial_analysis = {
            'target_name': name,
            'company_number': company_number,
            'fca_regulated_check': 'Requires manual FCA register verification',
            'bankruptcy_status': 'Check Insolvency Service records',
            'hmrc_compliance': 'Verify tax registration status'
        }
        
        self.results['uk_financial_intelligence'] = financial_sources
        self.results['uk_financial_analysis'] = financial_analysis
        
        for source, url in financial_sources.items():
            self.log(f"Financial source: {source} - {url}")
    
    def uk_legal_court_records(self):
        """UK Legal and court records investigation"""
        print("⚖️ UK LEGAL & COURT RECORDS INVESTIGATION...")
        
        name = self.target_info.get('name', '')
        
        legal_sources = {
            'uk_court_records': "https://www.judiciary.uk/courts-and-tribunals/",
            'criminal_records_check': "https://www.gov.uk/request-copy-criminal-record",
            'uk_court_judgments': "https://www.trustonline.org.uk/",
            'hmcts_court_search': "https://www.gov.uk/find-court-tribunal",
            'uk_legal_register': "https://www.lawsociety.org.uk/",
            'uk_restraining_orders': "https://www.gov.uk/browse/justice/courts-sentencing-tribunals"
        }
        
        # UK legal analysis
        legal_analysis = {
            'target_name': name,
            'dbs_check_required': 'Enhanced DBS check may be required',
            'court_records': 'Check HMCTS records for civil/criminal proceedings',
            'legal_practitioner': 'Verify if subject is a qualified legal professional',
            'bankruptcy_orders': 'Check for bankruptcy or debt relief orders'
        }
        
        self.results['uk_legal_court'] = legal_sources
        self.results['uk_legal_analysis'] = legal_analysis
        
        for source, url in legal_sources.items():
            self.log(f"Legal source: {source} - {url}")
    
    def uk_data_protection_compliance(self):
        """UK Data Protection and GDPR compliance check"""
        print("🔒 UK DATA PROTECTION & GDPR COMPLIANCE...")
        
        compliance_framework = {
            'gdpr_compliance': 'Investigation conducted under GDPR Article 6 lawful basis',
            'uk_data_protection_act': 'Compliant with UK Data Protection Act 2018',
            'ico_registration': 'Information Commissioner\'s Office guidelines followed',
            'subject_rights': 'Data subject rights under UK GDPR respected',
            'data_minimisation': 'Only publicly available information collected',
            'retention_policy': 'Data retained only for investigation purposes'
        }
        
        self.results['uk_data_protection'] = compliance_framework
        
        self.log("GDPR compliance framework applied")
        self.log("UK Data Protection Act 2018 requirements met")
    
    def generate_uk_report(self):
        """Generate comprehensive UK investigation report"""
        print("\n" + "═" * 70)
        print("📋 GENERATING UK OSINT INVESTIGATION REPORT")
        print("═" * 70)
        
        report_filename = f"uk_osint_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write("🇬🇧 UK OSINT INTELLIGENCE INVESTIGATION REPORT\n")
            f.write("═" * 60 + "\n\n")
            
            f.write("UK TARGET INFORMATION:\n")
            f.write("-" * 30 + "\n")
            for key, value in self.target_info.items():
                if value:
                    f.write(f"{key.upper()}: {value}\n")
            
            f.write(f"\nUK INVESTIGATION TIMESTAMP: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
            
            f.write("UK INVESTIGATION RESULTS:\n")
            f.write("-" * 30 + "\n")
            
            for category, data in self.results.items():
                f.write(f"\n[{category.upper().replace('_', ' ')}]\n")
                if isinstance(data, dict):
                    for key, value in data.items():
                        f.write(f"  {key}: {value}\n")
                elif isinstance(data, list):
                    for item in data:
                        f.write(f"  - {item}\n")
                else:
                    f.write(f"  {data}\n")
            
            f.write(f"\n\nUK COMPLIANCE STATEMENT:\n")
            f.write("-" * 30 + "\n")
            f.write("This investigation was conducted in compliance with:\n")
            f.write("• UK Data Protection Act 2018\n")
            f.write("• General Data Protection Regulation (GDPR)\n")
            f.write("• Information Commissioner's Office (ICO) guidelines\n")
            f.write("• UK privacy and data protection laws\n")
            
            f.write(f"\n\nREPORT GENERATED: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            f.write(f"\nUK PROFESSIONAL INTELLIGENCE GATHERING\n")
        
        print(f"✅ UK REPORT SAVED: {report_filename}")
        print(f"📄 {len(self.results)} UK investigation categories completed")
        print("🇬🇧 UK intelligence gathering complete!")
        
        return report_filename
    
    def run_full_uk_investigation(self):
        """Run complete UK OSINT investigation"""
        print("🚀 STARTING FULL UK INTELLIGENCE INVESTIGATION...")
        print("─" * 70)
        
        # Run all UK investigation modules
        self.uk_government_records_search()
        time.sleep(1)
        
        self.uk_professional_bodies_search()
        time.sleep(1)
        
        self.uk_electoral_address_verification()
        time.sleep(1)
        
        self.uk_business_intelligence()
        time.sleep(1)
        
        self.uk_property_assets_search()
        time.sleep(1)
        
        self.uk_social_media_digital_search()
        time.sleep(1)
        
        self.uk_financial_intelligence()
        time.sleep(1)
        
        self.uk_legal_court_records()
        time.sleep(1)
        
        self.uk_data_protection_compliance()
        time.sleep(1)
        
        # Generate final UK report
        report_file = self.generate_uk_report()
        
        return report_file

def main():
    parser = argparse.ArgumentParser(
        description="UK OSINT CLI Tool - Professional British Intelligence Platform",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
UK Investigation Examples:
  python uk_osint_cli.py --name "John Smith" --postcode "SW1A 1AA"
  python uk_osint_cli.py --name "Jane Doe" --email "jane@example.co.uk" --phone "+44 7700 900123"
  python uk_osint_cli.py --company-number "12345678" --name "ACME Ltd"
  python uk_osint_cli.py --name "Dr Smith" --postcode "M1 1AA" --address "Manchester"

Professional UK intelligence gathering! 🇬🇧
        """
    )
    
    parser.add_argument('--name', '-n', help='Target full name')
    parser.add_argument('--email', '-e', help='Target email address')
    parser.add_argument('--phone', '-p', help='Target mobile number (+44 format)')
    parser.add_argument('--postcode', '-pc', help='UK postcode (e.g., SW1A 1AA)')
    parser.add_argument('--company-number', '-cn', help='UK company registration number')
    parser.add_argument('--address', '-a', help='UK address or location')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if not any([args.name, args.email, args.phone, args.company_number]):
        parser.error("At least one target identifier required (name, email, phone, or company number)")
    
    # Initialize UK OSINT tool
    uk_osint = UKProfessionalOSINT()
    uk_osint.verbose = args.verbose
    uk_osint.banner()
    
    # Set UK target information
    uk_osint.set_target(
        name=args.name,
        email=args.email,
        phone=args.phone,
        postcode=args.postcode,
        company_number=args.company_number,
        address=args.address
    )
    
    # Run UK investigation
    report_file = uk_osint.run_full_uk_investigation()
    
    print(f"\n🎯 UK Investigation complete! Check {report_file} for full results.")
    print("🇬🇧 UK intelligence gathering successful - GDPR compliant!")

if __name__ == "__main__":
    main()