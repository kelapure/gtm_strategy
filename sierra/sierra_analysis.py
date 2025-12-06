#!/usr/bin/env python3
"""
Sierra $100M ARR Analysis Report Generator
Creates a professionally formatted PDF from the comprehensive analysis
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, NextPageTemplate, PageTemplate
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfgen.canvas import Canvas
from datetime import datetime
import os

class HeaderCanvas(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)

    def showPage(self):
        self._draw_header()
        Canvas.showPage(self)

    def _draw_header(self):
        # Page header
        self.setFont('Helvetica-Bold', 10)
        self.setFillColor(colors.grey)
        self.drawString(0.5 * inch, letter[1] - 0.5 * inch,
                       "Sierra $100M ARR Analysis - Forensic Reconstruction")

        # Page number
        page_num = f"Page {self._pageNumber}"
        self.drawRightString(letter[0] - 0.5 * inch, letter[1] - 0.5 * inch, page_num)

        # Line under header
        self.setStrokeColor(colors.grey)
        self.setLineWidth(0.5)
        self.line(0.5 * inch, letter[1] - 0.6 * inch,
                 letter[0] - 0.5 * inch, letter[1] - 0.6 * inch)

def create_sierra_analysis_pdf():
    """Create the complete Sierra analysis PDF with perfect formatting"""

    filename = "/Users/rohitkelapure/projects/sierra/Sierra_100M_ARR_Analysis.pdf"

    # Create document with custom canvas for headers
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=1*inch,
        bottomMargin=0.75*inch,
        canvasmaker=HeaderCanvas
    )

    # Get styles and create custom styles
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold'
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.grey,
        fontName='Helvetica-Oblique'
    )

    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=20,
        spaceBefore=20,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold',
        borderWidth=1,
        borderColor=colors.lightgrey,
        borderPadding=5
    )

    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=15,
        spaceBefore=15,
        textColor=colors.darkgreen,
        fontName='Helvetica-Bold'
    )

    h3_style = ParagraphStyle(
        'CustomH3',
        parent=styles['Heading3'],
        fontSize=12,
        spaceAfter=10,
        spaceBefore=10,
        textColor=colors.darkred,
        fontName='Helvetica-Bold'
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )

    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8,
        leftIndent=20,
        bulletIndent=10,
        fontName='Helvetica'
    )

    # Build story content
    story = []

    # Title page
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("Sierra AI", title_style))
    story.append(Paragraph("$100M ARR Forensic Analysis", subtitle_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Comprehensive Revenue Reconstruction", subtitle_style))
    story.append(Spacer(1, 1*inch))

    # Author and date
    author_style = ParagraphStyle(
        'Author',
        parent=styles['Normal'],
        fontSize=12,
        alignment=TA_CENTER,
        spaceAfter=10
    )

    story.append(Paragraph(f"Prepared by: Rohit Kelapure", author_style))
    story.append(Paragraph(f"Date: {datetime.now().strftime('%B %d, %Y')}", author_style))
    story.append(PageBreak())

    # Executive Summary
    story.append(Paragraph("a) Executive Summary", h1_style))

    story.append(Paragraph("1. What can and cannot be known", h2_style))

    bullet_points_1 = [
        "Public sources confirm that Sierra crossed roughly <b>$100M in ARR in November 2025</b>, 21 months / 7 quarters after launch in February 2024.",
        "A private‑markets analyst (Sacra) estimates ARR at <b>$104M</b> as of late 2025, up from <b>~$26M</b> in December 2024 and <b>> $20M</b> in annualized revenue in October 2024.",
        "Multiple reports agree Sierra now serves <b>\"hundreds of customers\"</b>, with a mix of internet-native firms (e.g., Deliveroo, Discord, Ramp, Rivian, SoFi, Tubi, Wayfair) and traditional enterprises (e.g., ADT, Bissell, Vans, Cigna, SiriusXM, DIRECTV, Safelite)."
    ]

    for point in bullet_points_1:
        story.append(Paragraph(f"• {point}", bullet_style))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Critically:</b>", body_style))

    critical_points = [
        "<b>No public source discloses contract‑by‑contract subscription amounts, customer‑level ARR, or specific churned logos.</b>",
        "All we can do \"forensically\" is (1) reconstruct the <b>revenue model</b> and timeline, and (2) map out <b>who is in production, doing what, with what performance metrics</b>. Any per‑customer dollar attribution would be pure speculation. I will not do that."
    ]

    for point in critical_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    # Revenue model section
    story.append(Paragraph("2. Revenue model and ARR drivers", h2_style))

    revenue_points = [
        "Sierra's revenue comes primarily from <b>usage‑ and outcome‑based contracts</b>: customers pay <b>per conversation or per successful resolution / outcome</b>, often bundled with implementation and optimization in <b>multi‑year enterprise agreements</b>.",
        "The company positions this as <b>\"outcome‑based pricing\"</b>: they charge when the agent successfully completes a defined job (resolved support conversation, saved cancellation, upsell, cross‑sell, etc.); in most cases, unresolved conversations are not billed.",
        "External analyses describe <b>per‑resolution economics</b> tied to the avoided cost of a human agent: one essay notes Sierra earning a <b>set fee per AI‑resolved call linked to the $10–$20 cost avoided per deflection</b>, and another Chinese‑language analysis uses an illustrative <b>$1 per successful resolution to save $10</b> example.",
        "A Verge interview with Bret Taylor clarifies that Sierra's ARR is calculated like a traditional enterprise SaaS company: <b>12‑month+ contracts, often multi‑year, billed annually up front with net‑30 payment terms</b>, not month‑to‑month usage multiplied by 12.",
        "Sacra confirms that revenue in 2025 is <b>\"primarily from usage‑ and outcome‑based contracts\"</b> layered into multi‑year deals, with voice interactions now accounting for the majority of traffic."
    ]

    for point in revenue_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    # Key customers section
    story.append(Paragraph("3. Key customers and use cases (high level)", h2_style))

    story.append(Paragraph("Across public materials, a consistent cohort of <b>large, brand‑name customers</b> show up in multiple independent sources (Sierra's own content plus press/analyst/partner posts). Their agents collectively form the most credible basis for the $100M ARR:", body_style))

    customer_segments = [
        "<b>Financial services / fintech</b> – SoFi, Ramp, Brex, Chime, Marshmallow, Rocket Mortgage, Cigna, plus other unnamed banks and insurers. Agents handle card replacement, account servicing, authentication, disputes, policy changes, cancellations/retention, and mortgage origination.",
        "<b>Retail / consumer / CPG</b> – Wayfair, Tubi, Sonos, OluKai, Chubbies, Wilson, Minted, Casper, Thrive Market, AG1, Pendulum, Sun & Ski Sports. Agents handle order status, exchanges/returns, product recommendations and sizing, subscription changes, and high‑volume seasonal spikes (Black Friday, holidays).",
        "<b>Media / telecom</b> – SiriusXM, DIRECTV, AOL, Fox, Tubi (media). Agents manage subscription changes, billing, password resets, and troubleshooting.",
        "<b>Security / identity / infrastructure</b> – ADT, CLEAR, CDW. Agents handle alarm troubleshooting, billing, appointment scheduling, member services, and complex B2B IT support for hundreds of thousands of customers."
    ]

    for segment in customer_segments:
        story.append(Paragraph(f"• {segment}", bullet_style))

    # Monetization section
    story.append(Paragraph("4. Monetization vs. per‑customer amounts", h2_style))

    monetization_points = [
        "Public sources <b>do not disclose</b> how much SoFi, Wayfair, SiriusXM, etc. each pay. Even investor memos and ARR write‑ups speak only in <b>aggregate</b> (e.g., ARR, valuations, funding size).",
        "Where numeric hints exist, they are <b>economic analogies, not pricing sheets</b> (e.g., \"$10–$20 avoided cost per deflected call,\" \"pay $1 to save $10\"). Those demonstrate the <b>unit economics</b> but not contract sizes or logo‑level ARR.",
        "Therefore, from a forensic standpoint, we can say <b>which customers are in production, what they use Sierra for, and what operational metrics they report</b>, but <b>not</b> \"SoFi contributes $X to ARR\" or \"Tubi's subscription is $Y per year.\" Any such numbers would be invented."
    ]

    for point in monetization_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    # Churn section
    story.append(Paragraph("5. Churn", h2_style))

    churn_points = [
        "I see <b>no public disclosures</b> of specific customers that have churned from Sierra. On the contrary, most evidence is of <b>expanding relationships</b> (e.g., WeightWatchers and SiriusXM taking on more channels / data platforms; Brex, Ramp, and Thrive Market expanding use cases; Rocket Mortgage shipping additional journeys; Safelite extending from consumer to insurer programs).",
        "There are user complaints about AI support generally (and some social posts referencing \"Sierra\" in a negative tone in the context of Deliveroo riders), but nothing that credibly documents <b>a named Sierra customer terminating its contract with Sierra and moving away</b>.",
        "Without filings or direct statements, any claim that \"X customer churned for Y reason\" would be conjecture."
    ]

    for point in churn_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("In short: we can <b>forensically reconstruct Sierra's revenue mechanics and customer footprint</b> around the $100M ARR mark, but <b>not</b> a logo‑by‑logo dollar breakdown or a list of churned customers with causes.", body_style))

    story.append(PageBreak())

    # Structured breakdown section
    story.append(Paragraph("b) Structured breakdown", h1_style))

    # ARR Timeline table
    story.append(Paragraph("1. ARR and capital timeline", h2_style))

    arr_timeline_data = [
        ['Date (approx)', 'Metric', 'Amount / fact', 'Sources'],
        ['Oct 2024', 'Annualized revenue', 'Crossed about $20M in annualized revenue', 'Sacra'],
        ['Dec 2024', 'ARR estimate', 'Sacra estimates ~$26M ARR', 'Sacra'],
        ['Sep 2025', 'Funding', '$350M round led by Greenoaks at $10B valuation;\nSierra "on track to exceed $100M enterprise ARR"', 'Sierra'],
        ['Nov 5 2025', 'Product & scale', 'Agent OS 2.0 announced; voice agents handling\nhundreds of millions of calls', 'Sacra'],
        ['Nov 21 2025', 'ARR milestone', 'Sierra blog: $100M ARR in 7 quarters;\nTech / SaaS media confirm', 'Sierra'],
        ['Nov 2025', 'ARR estimate', 'Sacra: $104M ARR, up 4x from late 2024', 'Sacra'],
        ['Dec 4 2025', 'Strategic funding', 'Additional investment from SoftBank Vision Fund 2\nfor Japan expansion; confirms >$100M run‑rate', 'Axios']
    ]

    arr_table = Table(arr_timeline_data, colWidths=[1.2*inch, 1.3*inch, 3.2*inch, 1*inch])
    arr_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))

    story.append(arr_table)
    story.append(Spacer(1, 0.3*inch))

    # Revenue mechanics table
    story.append(Paragraph("2. Revenue mechanics", h2_style))

    revenue_mechanics_data = [
        ['Component', 'Description', 'Evidence'],
        ['Outcome‑based pricing', 'Pay per successful outcome (resolved conversation,\ncancellation saved, upsell, cross‑sell). No charge in\nmost cases for unresolved conversations.', 'Sierra'],
        ['Usage‑based pricing', 'For some flows (e.g., greeter / routing), pricing\ncan be volume‑based per conversation rather than\noutcome‑linked; blended structures are used in practice.', 'Sierra'],
        ['Multi‑year, upfront\ncontracts', 'Contracts are 12+ months, often multi‑year, billed\nannually up front with net‑30 payment terms;\nresembles public SaaS firms\' revenue recognition.', 'The Verge'],
        ['Unit economics', 'Analysts describe Sierra earning a fixed fee per\nresolved call tied to the $10–$20 cost avoided for\na human‑handled ticket; another article uses an\nexample of paying ~$1 per successful resolution to save ~$10.', 'lennysvault.com'],
        ['Services /\nimplementation', 'Revenue includes high‑touch implementation and\nongoing optimization, bundled into enterprise\nagreements, rather than sold alone.', 'Sacra'],
        ['Channel mix', 'Voice has overtaken text as primary channel by\nSept 2025, implying a large share of revenue from\nAI phone calls handled per minute or per resolution.', 'Sacra']
    ]

    revenue_table = Table(revenue_mechanics_data, colWidths=[1.5*inch, 3.5*inch, 1.7*inch])
    revenue_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))

    story.append(revenue_table)
    story.append(PageBreak())

    # Major customers section
    story.append(Paragraph("3. Major customers, use cases, and metrics", h2_style))

    story.append(Paragraph("Below is a <b>sample of large, repeatedly‑named customers</b> that are credibly in production with Sierra. For each, I include at least two independent sources (Sierra + external where available). \"$ Subscription amount\" is marked <b>Not disclosed</b> whenever no credible figure exists; that is the case for all rows.", body_style))

    # Financial services table
    story.append(Paragraph("Financial services & fintech", h3_style))

    fintech_data = [
        ['Customer', 'Use case summary', 'Key metrics disclosed', '$ subscription amount', 'Evidence'],
        ['SoFi', 'Consumer fintech / bank – AI agent\nfor member support across account,\ncards, payments', 'Named as major Sierra client; cited\nas one of the "major clients" whose\nmulti‑year contracts underpin the $100M ARR.', 'Not disclosed', 'Sierra ARR blog lists SoFi among\nflagship customers. Third‑party\ncoverage lists SoFi as active Sierra client.'],
        ['Ramp', 'Corporate card / spend management\n– AI agent automating support,\ncard replacement, admin workflows', '90% case‑resolution via automation;\nrolling out voice agent.', 'Not disclosed', 'Sierra Ramp case study. Sierra\ncustomers page & LinkedIn posts\nemphasize Ramp as a flagship fintech.'],
        ['Brex', 'Fintech – "Change agents: Brex"\ncustomer agent for finance ops\n& customer service', 'Blog states AI agent has accelerated\nservice by ~90% and saved customers\n>15,000 hours/year.', 'Not disclosed', 'Sierra "Change agents: Brex" blog.\nInvestor write‑ups list Brex as one\nof the flagship fintechs.'],
        ['Chime', 'Neobank – AI agents as 24/7\n"brand extensions" for member questions', 'Reported resolution increase from\n50% → 70%, with better hallucination\nresistance than prior tools.', 'Not disclosed', 'Sierra "Change agents: Chime" blog.\nExecsInTheKnow article confirms\nChime partnership and performance gains.'],
        ['Marshmallow (UK)', 'Motor insurance – agent "Marsha"\nhandles quotes, renewals, policy\nupdates, multilingual regulated support', 'CSAT 82% on AI‑handled conversations;\n"significant share" of service volume,\n24/7, multilingual.', 'Not disclosed', 'Sierra Marshmallow customer page\n& sector pages. Sierra LinkedIn\nannouncement with performance stats.']
    ]

    fintech_table = Table(fintech_data, colWidths=[1*inch, 1.8*inch, 1.8*inch, 1*inch, 1.9*inch])
    fintech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))

    story.append(fintech_table)
    story.append(Spacer(1, 0.3*inch))

    # Retail/DTC table
    story.append(Paragraph("Retail / DTC / CPG", h3_style))

    retail_data = [
        ['Customer', 'Use case summary', 'Key metrics disclosed', '$ subscription amount', 'Evidence'],
        ['Tubi', 'AVOD streaming – subscriber\nsupport, account & device issues', 'Reported ~80% containment and\n+7 percentage‑point CSAT improvement\nafter Sierra deployment.', 'Not disclosed', 'Sierra Tubi case study and\nmedia‑industry page. LinkedIn posts\nquoting containment & CSAT uplift.'],
        ['Sonos', 'Consumer electronics – support\nacross channels to reduce "time‑to‑music"', 'Agents support 15M customers;\nfocus on setup/troubleshooting\nacross complex home networks.', 'Not disclosed', 'Sierra Sonos case study and holiday blog.\nExternal tech/business coverage names\nSonos as one of Sierra\'s early customers.'],
        ['OluKai', 'Footwear – "Aloha Experience" support', 'Sierra handles ~70% of service tickets;\nused heavily for holiday launches;\nre‑applied patterns to other brands.', 'Not disclosed', 'Sierra OluKai case + holiday blog.\nLinkedIn posts from Sierra and\nOluKai leadership discussing results.'],
        ['Wilson', 'Sporting goods – equipment\n& custom orders', 'Agent has resolved tens of thousands\nof conversations with >77% containment.', 'Not disclosed', 'Wilson customer story + Sierra\ncustomers page.'],
        ['Thrive Market', 'Membership retail – member support,\nsubscriptions, experimentation', 'Reported >50% improvement in case\nresolution and ~90% CSAT on\nAI interactions.', 'Not disclosed', 'Sierra Thrive Market case study\n+ LinkedIn posts.']
    ]

    retail_table = Table(retail_data, colWidths=[1*inch, 1.8*inch, 1.8*inch, 1*inch, 1.9*inch])
    retail_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))

    story.append(retail_table)
    story.append(Spacer(1, 0.3*inch))

    # Media/telecom table
    story.append(Paragraph("Media, telecom, and identity", h3_style))

    media_data = [
        ['Customer', 'Use case summary', 'Key metrics', '$ subscription amount', 'Evidence'],
        ['SiriusXM', 'Audio subscription – "Harmony" AI agent,\nfirst adopter of Agent Data Platform', 'Serves 34M subscribers; millions of\ncustomer enquiries; now first customer\nfor Sierra\'s Agent Data Platform.', 'Not disclosed', 'Sierra SiriusXM case + ADP announcement.\nAxios & other coverage cite SiriusXM\nas a flagship Sierra customer.'],
        ['DIRECTV', 'Pay‑TV – subscriber support', 'Listed as key customer on site;\nfeatured in Summit media/telecom content.', 'Not disclosed', 'Sierra site and homepage logos.\nLinear\'s overview lists DIRECTV\namong major brands using Sierra agents.'],
        ['CLEAR', 'Identity / travel', 'Member hospitality & retention engine;\nCSAT 4.7/5 for AI‑handled interactions.', 'Not disclosed', 'Sierra CLEAR customer story and\nindustry/product pages. External\nanalysis notes CLEAR as a Sierra customer.']
    ]

    media_table = Table(media_data, colWidths=[1*inch, 2*inch, 2*inch, 1*inch, 2.5*inch])
    media_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.purple),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lavender),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))

    story.append(media_table)
    story.append(PageBreak())

    # Security/B2B table
    story.append(Paragraph("Security, infra & B2B", h3_style))

    security_data = [
        ['Customer', 'Use case summary', 'Key metrics', '$ subscription amount', 'Evidence'],
        ['ADT', 'Home security – 24/7 alarm & account\nsupport; "every second counts"', '2M+ customer inquiries per month;\nAI agent handles troubleshooting,\naccount changes, and (soon) payments\n& service orders.', 'Not disclosed', 'Sierra ADT case + "What is an AI agent?"\nexamples. Medium and LinkedIn posts\nconfirm ADT deploying Sierra agent.'],
        ['CDW', 'B2B IT reseller – complex support\nfor 250k+ customers', 'Sierra agent used for procurement /\nIT support; Taylor notes 250K customers\nserved and highlights B2B CX improvements.', 'Not disclosed', 'Sierra CDW customer story.\nTaylor\'s LinkedIn post corroborates\npartnership and scale.'],
        ['Safelite', 'Auto glass – consumer & insurer claims', '"Scarlett" agent handles auto‑glass claims;\nSierra + Safelite also launching\nAgent‑Maker program for insurers.', 'Not disclosed', 'Sierra "Change agents: Safelite" blog;\nCEO Renee Cacchillo profile. External\nposts highlight the Safelite partnership.']
    ]

    security_table = Table(security_data, colWidths=[1*inch, 2*inch, 2.2*inch, 1*inch, 2.3*inch])
    security_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.mistyrose),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))

    story.append(security_table)
    story.append(Spacer(1, 0.3*inch))

    # Churn and risk table
    story.append(Paragraph("4. Churn and risk indicators", h2_style))

    churn_data = [
        ['Item', 'What we can see', 'Forensic assessment'],
        ['Named customer churn', 'No public reports of specific named customers\n(SoFi, Wayfair, WeightWatchers, Sonos, etc.)\ndiscontinuing Sierra.', 'We cannot identify any logo that has clearly\nchurned from Sierra based on public data.'],
        ['Negative end‑user\nsentiment', 'Some posts (e.g., Deliveroo driver forums,\ngeneral AI‑support complaints) show frustration\nwith AI agents and mention "Sierra" generically\nin delivering poor support.', 'Indicates experience risk but not confirmed\nenterprise churn. These are end‑user anecdotes,\nnot corporate termination announcements.'],
        ['Pricing / complexity\ncritiques', 'Independent reviews describe Sierra as powerful\nbut with "opaque pricing" and a steep learning\ncurve, positioning it as a fit for teams with\nstrong engineering and CX resources.', 'Suggests a risk of future churn among smaller\nor less technical customers; no concrete\nlogo‑level churn disclosed.'],
        ['Retention signals', 'Numerous case studies and posts show customers\nexpanding use (more channels, voice, new\njourneys, adoption of Agent Data Platform).', 'Expansion behavior is consistent with strong\nnet revenue retention, but exact NRR is not disclosed.']
    ]

    churn_table = Table(churn_data, colWidths=[1.5*inch, 2.8*inch, 2.8*inch])
    churn_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.wheat),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))

    story.append(churn_table)
    story.append(PageBreak())

    # Narrative report section
    story.append(Paragraph("c) Narrative report (forensic-style)", h1_style))

    story.append(Paragraph("1. Mandate and approach", h2_style))
    story.append(Paragraph("You asked for an SEC‑grade reconstruction of how Sierra reached $100M in ARR in seven quarters, including:", body_style))

    mandate_points = [
        "Sources of revenue and ARR structure",
        "Identification of customers, their use cases, and subscription amounts",
        "Identification of churned customers and reasons"
    ]

    for point in mandate_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    story.append(Paragraph("Given Sierra is private, with no public 10‑K/10‑Q equivalents, I rely on:", body_style))

    source_points = [
        "Sierra's own blogs, product/industry pages, and customer case studies",
        "Third‑party analyst and investor research (Sacra, MLQ, etc.)",
        "Press and commentary (Verge, Axios, Yahoo Finance, TechCrunch, TechBuzz, etc.)",
        "Public social posts (LinkedIn, X) from Sierra, customers, and investors"
    ]

    for point in source_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    # Revenue curve reconstruction
    story.append(Paragraph("2. Reconstructing the ARR curve", h2_style))

    story.append(Paragraph("Sacra's private‑markets profile provides the most concrete, quantitative revenue trajectory:", body_style))

    trajectory_points = [
        "<b>2024</b> – Sierra is founded in 2023, launches in early 2024, and by October 2024 has \"crossed about $20M\" in annualized revenue. Sacra estimates $26M ARR by December 2024.",
        "<b>2025</b> – As enterprises scale pilots into production across chat and especially voice, Sacra estimates that ARR has grown >4x to around $104M by November 2025."
    ]

    for point in trajectory_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    story.append(Paragraph("Sierra's own blog then publicly confirms that they have \"just hit <b>$100M in ARR</b> — seven quarters after we launched in February 2024,\" calling themselves one of the fastest‑growing enterprise software companies in history.", body_style))

    story.append(Paragraph("From this, the most reasonable reconstruction is:", body_style))

    reconstruction_points = [
        "Late 2024: ARR in the <b>low tens of millions</b> ($20–$30M range), as pilots go live.",
        "Mid‑2025: ARR passing <b>$50–$70M</b>, consistent with \"on track to exceed $100M ARR\" in Axios's September funding scoop.",
        "November 2025: ARR at <b>$100M+</b>, with Sacra's $104M estimate within noise of Sierra's own $100M claim."
    ]

    for point in reconstruction_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    # Revenue model section
    story.append(Paragraph("3. Revenue model: why ARR looks like classic enterprise SaaS", h2_style))

    story.append(Paragraph("Although Sierra is marketing itself as a radically new \"agentic AI\" platform, their <b>revenue mechanics</b> are deliberately conservative:", body_style))

    conservative_points = [
        "<b>Contract structure</b> – Bret Taylor states that Sierra follows traditional enterprise norms: 12‑month minimum terms, often multi‑year, billed annually up front, with 30 days for the customer to pay the invoice.",
        "<b>Consumption unit</b> – Instead of seats or tokens, Sierra charges per successful outcome (per resolution, cancellation saved, or transaction). Their own blog on outcome‑based pricing defines this clearly.",
        "<b>Blended usage/outcome pricing</b> – For some flows (e.g., greeters and routing), Sierra uses per‑conversation usage pricing, blending outcome‑based and usage‑based fees in the same agreement."
    ]

    for point in conservative_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    story.append(Paragraph("Third‑party analyses offer hints about the <b>unit economics</b>:", body_style))

    economics_points = [
        "Lenny's insights vault notes that Sierra collects a set fee per AI‑resolved call, economically tied to the $10–$20 cost the customer avoids per deflected human call.",
        "A Chinese‑language industry piece describes Sierra's outcome‑based model as \"pay only when the agent delivers a valuable outcome\" and uses an example of paying $1 per successful resolution to save $10 of manual cost."
    ]

    for point in economics_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    story.append(Paragraph("Neither source gives precise list pricing, but together they make the economics clear: <b>Sierra's fee per resolution is set as a fraction of the avoided human cost</b>, so large enterprises with millions of calls can easily generate <b>multi‑million‑dollar annual contracts</b> without publishing a public per‑seat or per‑token price.", body_style))

    # Continue with remaining sections...
    story.append(Paragraph("4. Customers and use cases as ARR drivers", h2_style))

    story.append(Paragraph("The $100M ARR is, in practice, <b>the sum of a relatively small number of very large deployments plus a long tail of other enterprises</b>. The most heavily‑publicized customers cluster in a few sectors:", body_style))

    cluster_points = [
        "<b>Fintech / financial services</b> – SoFi, Ramp, Brex, Chime, Marshmallow, Rocket Mortgage, Cigna, plus other unnamed banks and insurers in the U.S. and Europe.",
        "<b>Retail & DTC</b> – Wayfair, Tubi, Sonos, OluKai, Chubbies, Wilson, Minted, Casper, Thrive Market, AG1, Pendulum, Sun & Ski, various others.",
        "<b>Media & telecom</b> – SiriusXM, DIRECTV, AOL, FOX‑related properties, plus Tubi as both media and DTC.",
        "<b>Security / infra / identity</b> – ADT, CLEAR, CDW, Safelite."
    ]

    for point in cluster_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    story.append(Paragraph("For nearly all of these customers, Sierra and/or the customer publishes <b>hard performance metrics</b> (containment rates, CSAT, case‑resolution share, conversion lift, cancellation reduction), but <b>never dollar figures</b>. Examples:", body_style))

    metrics_examples = [
        "Ramp: <b>90%</b> of cases fully resolved by the agent.",
        "WeightWatchers: ~<b>70% containment</b> with <b>CSAT > 4.5/5</b>.",
        "Tubi: <b>~80% containment</b> and <b>+7 CSAT points</b> vs. baseline.",
        "Wilson: <b>>77% containment</b> on tens of thousands of conversations.",
        "Thrive Market: <b>>50% case‑resolution improvement</b> and <b>~90% CSAT</b> for AI‑handled interactions."
    ]

    for example in metrics_examples:
        story.append(Paragraph(f"• {example}", bullet_style))

    story.append(Paragraph("From a revenue‑forensics standpoint, these numbers matter because they show how Sierra can justify <b>large outcome‑based contracts</b>:", body_style))

    justification_points = [
        "A customer like <b>ADT</b> with <b>2M+ monthly inquiries</b> can route a large fraction through Sierra at a per‑resolution fee that still undercuts human support costs.",
        "A customer like <b>SiriusXM</b> with <b>34M subscribers</b> and millions of enquiries per year can define resolution and retention outcomes that materially move revenue, then pay Sierra only when those outcomes are achieved."
    ]

    for point in justification_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    story.append(Paragraph("It is entirely plausible that <b>a few dozen such customers account for the majority of the $100M ARR</b>, but because contract values are not disclosed, we cannot decompose that ARR logo‑by‑logo.", body_style))

    # Subscription amounts section
    story.append(Paragraph("5. Subscription amounts: what we can infer—and what we can't", h2_style))

    story.append(Paragraph("You explicitly asked for each customer's <b>subscription amount</b>. Here's what the evidence allows:", body_style))

    evidence_points = [
        "We know the <b>total</b> (≈$100M ARR) and we know many of the <b>logos</b> contributing to it.",
        "We know the <b>pricing unit</b> (per successful resolution/outcome or per conversation), typical <b>economic framing</b> (save $10–$20 of cost per deflected call; pay a fraction of that to Sierra), and <b>contract structure</b> (multi‑year, annual upfront).",
        "What we <b>do not</b> have: any public figure like \"SoFi pays $X per year\" or \"SiriusXM contract is $Y over Z years.\" Neither Sierra, the customers, nor analysts have published those numbers."
    ]

    for point in evidence_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    story.append(Paragraph("Therefore, the only honest statement is:", body_style))
    story.append(Paragraph("<i>All currently available public information is <b>insufficient to assign per‑customer subscription amounts or logo‑level ARR</b>. We can only describe <b>how</b> Sierra monetizes each customer, not <b>how much</b> revenue each contributes.</i>", body_style))

    # Churn analysis section
    story.append(Paragraph("6. Churn analysis", h2_style))

    story.append(Paragraph("You also asked to \"identify the customers that churned and the reasons why.\"", body_style))
    story.append(Paragraph("Based on the corpus examined:", body_style))

    churn_findings = [
        "<b>No article, blog, or analyst report</b> claims that a named customer (e.g., WeightWatchers, Sonos, SiriusXM, SoFi, Wayfair, ADT) <b>has left Sierra</b>. On the contrary, many stories are framed as <b>expansion</b> (additional channels, new products like Agent Data Platform, more complex journeys).",
        "End‑user complaints exist, including Deliveroo riders frustrated with an \"AI agent Sierra\" not solving issues, but these do not show Deliveroo abandoning Sierra; they show operational friction at the edge.",
        "Independent reviews criticize <b>opaque pricing and learning curve</b>, positioning Sierra as suitable mainly for well‑resourced teams; that suggests potential future churn among smaller or mismatched customers, but again, no logos are named."
    ]

    for finding in churn_findings:
        story.append(Paragraph(f"• {finding}", bullet_style))

    story.append(Paragraph("Given SEC‑style evidentiary standards, the correct conclusion is:", body_style))

    conclusion_points = [
        "<b>Known churned customers: none (publicly disclosed).</b>",
        "<b>Likely reasons for eventual churn (inferred, not observed):</b> pricing opacity, implementation complexity, or dissatisfaction with AI support quality—risks that appear in general commentary but not tied to specific departures."
    ]

    for point in conclusion_points:
        story.append(Paragraph(f"• {point}", bullet_style))

    story.append(Paragraph("Any statement like \"X churned because Y\" would go beyond the evidence and into conjecture.", body_style))

    # Overall conclusion
    story.append(Paragraph("7. Overall forensic conclusion", h2_style))

    final_conclusions = [
        "Sierra's <b>$100M+ ARR</b> is real and well‑corroborated across the company's own disclosures, investor/analyst estimates, and independent media.",
        "The ARR is driven by <b>a relatively small set of very large outcome‑based and usage‑based contracts</b> with prominent enterprise customers across fintech, retail/DTC, media, telecom, and security/identity. These contracts monetize <b>per resolution / per conversation</b>, not per seat.",
        "Public data is rich in <b>operational metrics</b> (containment, CSAT, cancellations saved, conversion lift) but <b>contains no logo‑level dollar amounts or explicit churn events</b>. That prevents a granular allocation of the $100M ARR by customer or an evidence‑based churn table."
    ]

    for conclusion in final_conclusions:
        story.append(Paragraph(f"• {conclusion}", bullet_style))

    story.append(Paragraph("If you want, the next logical step would be to build a <b>scenario model</b>: for example, assume a distribution of contract sizes across the identified customers (e.g., a handful of $5–$10M ARR \"whales,\" more $1–3M \"elephants,\" and a long tail), and explore what per‑resolution or per‑call pricing that would imply. That would necessarily be <b>hypothetical</b>, but we can keep it consistent with the published unit‑economics constraints.", body_style))

    # Build the PDF
    doc.build(story)

    return filename

if __name__ == "__main__":
    pdf_file = create_sierra_analysis_pdf()
    print(f"Sierra analysis PDF created successfully: {pdf_file}")