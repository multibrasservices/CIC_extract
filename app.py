
import streamlit as st
import pandas as pd
import pdfplumber
from io import BytesIO
import base64
from openpyxl.styles import NamedStyle
from openpyxl.utils import get_column_letter

def extract_data_from_pdf(file):
    """
    Extracts transaction data from a single PDF file with robust date checking.
    """
    transactions = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            # Use extract_table with table settings for better parsing
            table = page.extract_table()
            if table:
                for row in table:
                    # Ensure row is a list and has enough columns
                    if not isinstance(row, list) or len(row) < 5:
                        continue

                    # Robustly check if the first column is a valid date
                    try:
                        pd.to_datetime(row[0], format='%d/%m/%Y', errors='raise')
                        date = row[0]
                    except (ValueError, TypeError, IndexError):
                        # This row does not start with a valid date, so we skip it
                        continue
                    
                    # If we have a valid date, we can assume it's a transaction row
                    try:
                        libelle = row[2]
                        debit_str = row[3]
                        credit_str = row[4]

                        amount = 0.0
                        if debit_str and debit_str.strip():
                            amount = -float(debit_str.replace('.', '').replace(',', '.'))
                        elif credit_str and credit_str.strip():
                            amount = float(credit_str.replace('.', '').replace(',', '.'))

                        # Only add rows with a non-zero amount
                        if amount != 0.0:
                            transactions.append([date, libelle, amount])
                    except (ValueError, IndexError):
                        # Skip rows that look like transactions but have parsing issues
                        continue
    return transactions

def to_excel(df):
    """
    Converts a DataFrame to an Excel file in memory, with auto-width and currency formatting.
    """
    output = BytesIO()
    df_copy = df.copy()
    df_copy['date'] = df_copy['date'].dt.strftime('%d/%m/%y')

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_copy.to_excel(writer, index=False, sheet_name='Transactions')

        workbook = writer.book
        worksheet = writer.sheets['Transactions']

        # Define and add the currency style to the workbook
        currency_style = NamedStyle(name='currency_style', number_format='#,##0.00 €')
        if currency_style.name not in workbook.style_names:
            workbook.add_named_style(currency_style)

        # Auto-adjust columns and apply formats
        for idx, col in enumerate(worksheet.columns, 1):
            column_letter = get_column_letter(idx)
            max_length = 0
            
            # Find the maximum length of a cell in the column
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            
            # Adjust the column width
            adjusted_width = max_length + 2
            worksheet.column_dimensions[column_letter].width = adjusted_width

            # Apply currency format to 'debit' and 'credit' columns
            header_cell = worksheet.cell(row=1, column=idx)
            if header_cell.value in ('debit', 'credit'):
                # Apply the style to all cells in the column except the header
                for cell in col[1:]:
                    cell.style = currency_style

    processed_data = output.getvalue()
    return processed_data

st.set_page_config(layout="wide")

st.title("📄 Extracteur de Relevés Bancaires CIC")
st.write("Cette application Streamlit permet d'extraire les transactions de relevés bancaires PDF de la banque CIC et de les exporter dans un fichier Excel propre et formaté")

st.info("Chargez un ou plusieurs relevés de compte au format PDF pour extraire les opérations.")

uploaded_files = st.file_uploader(
    "Sélectionnez vos fichiers PDF", 
    type="pdf", 
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("🚀 Extraire et Traiter les Données", type="primary"):
        with st.spinner("Extraction des données en cours... Veuillez patienter."):
            all_transactions = []
            for uploaded_file in uploaded_files:
                try:
                    # Pass the file object directly
                    transactions = extract_data_from_pdf(uploaded_file)
                    all_transactions.extend(transactions)
                except Exception as e:
                    st.error(f"Erreur lors du traitement du fichier {uploaded_file.name}: {e}")

            if all_transactions:
                # Simplified DataFrame creation from the new function output
                df = pd.DataFrame(all_transactions, columns=['date_str', 'libelle', 'montant'])
                
                # Create the final DataFrame with correct types and separate debit/credit columns
                df_final = pd.DataFrame({
                    'date': pd.to_datetime(df['date_str'], format='%d/%m/%Y'),
                    'libelle': df['libelle'],
                    'debit': df['montant'].apply(lambda x: x if x < 0 else 0),
                    'credit': df['montant'].apply(lambda x: x if x > 0 else 0)
                })
                
                df_final = df_final.sort_values(by='date').reset_index(drop=True)

                st.success(f"✅ {len(df_final)} transactions extraites avec succès !")
                
                st.dataframe(df_final.style.format({
                    "debit": "{:.2f} €",
                    "credit": "{:.2f} €",
                    "date": "{:%d/%m/%Y}"
                }))

                excel_data = to_excel(df_final)
                st.download_button(
                    label="📥 Télécharger le fichier Excel",
                    data=excel_data,
                    file_name="transactions_cic.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.warning("Aucune transaction n'a pu être extraite des fichiers fournis.")
else:
    st.warning("Veuillez charger au moins un fichier PDF.")

# Footer with Logo, Version, and Copyright
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_img_with_href(local_img_path):
    img_format = local_img_path.split('.')[-1]
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'<img src="data:image/{img_format};base64,{bin_str}" width="100" />'
    return html_code

logo_html = get_img_with_href('assets/mon_logo.png')

footer_css = """
<style>
    .footer {
        position: fixed;
        right: 10px;
        bottom: 10px;
        text-align: right;
        color: grey;
    }
</style>
"""

footer_html = f"""
<div class="footer">
    {logo_html}
    <p>Version 1.0<br>
    &copy; 2025 - Tous droits réservés</p>
</div>
"""

st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)
