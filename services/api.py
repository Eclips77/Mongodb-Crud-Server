from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from services.dal import DocumentDAL
from services.solider_entity import Document

app = FastAPI(title="Document Management API", version="1.0.0")
dal = DocumentDAL()

class DocumentCreate(BaseModel):
    """
    Pydantic model for document creation
    """
    first_name: str
    last_name: str
    phone_number: str
    rank: str

class DocumentUpdate(BaseModel):
    """
    Pydantic model for document updates
    """
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    rank: Optional[str] = None

class DocumentResponse(BaseModel):
    """
    Pydantic model for document responses
    """
    id: str
    first_name: str
    last_name: str
    phone_number: str
    rank: str

@app.post("/documents/", response_model=DocumentResponse)
async def create_document(document_data: DocumentCreate):
    """
    Create a new document
    
    Args:
        document_data (DocumentCreate): Document data to create
        
    Returns:
        DocumentResponse: Created document
    """
    try:
        document = Document(
            first_name=document_data.first_name,
            last_name=document_data.last_name,
            phone_number=document_data.phone_number,
            rank=document_data.rank
        )
        
        success = dal.create(document)
        if success:
            return DocumentResponse(
                id=document.id,
                first_name=document.first_name,
                last_name=document.last_name,
                phone_number=document.phone_number,
                rank=document.rank
            )
        else:
            raise HTTPException(status_code=500, detail="Failed to create document")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/documents/{doc_id}", response_model=DocumentResponse)
async def get_document(doc_id: str):
    """
    Get a document by ID
    
    Args:
        doc_id (str): Document ID
        
    Returns:
        DocumentResponse: Found document
    """
    document = dal.read(doc_id)
    if document:
        return DocumentResponse(
            id=document.id,
            first_name=document.first_name,
            last_name=document.last_name,
            phone_number=document.phone_number,
            rank=document.rank
        )
    else:
        raise HTTPException(status_code=404, detail="Document not found")

@app.get("/documents/", response_model=List[DocumentResponse])
async def get_all_documents():
    """
    Get all documents
    
    Returns:
        List[DocumentResponse]: List of all documents
    """
    documents = dal.get_all()
    return [
        DocumentResponse(
            id=doc.id,
            first_name=doc.first_name,
            last_name=doc.last_name,
            phone_number=doc.phone_number,
            rank=doc.rank
        ) for doc in documents
    ]

@app.put("/documents/{doc_id}", response_model=dict)
async def update_document(doc_id: str, update_data: DocumentUpdate):
    """
    Update a document by ID
    
    Args:
        doc_id (str): Document ID
        update_data (DocumentUpdate): Data to update
        
    Returns:
        dict: Success message
    """
    update_dict = {k: v for k, v in update_data.dict().items() if v is not None}
    
    if not update_dict:
        raise HTTPException(status_code=400, detail="No data provided for update")
    
    success = dal.update(doc_id, update_dict)
    if success:
        return {"message": "Document updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Document not found or update failed")

@app.delete("/documents/{doc_id}", response_model=dict)
async def delete_document(doc_id: str):
    """
    Delete a document by ID
    
    Args:
        doc_id (str): Document ID
        
    Returns:
        dict: Success message
    """
    success = dal.delete(doc_id)
    if success:
        return {"message": "Document deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Document not found")

@app.on_event("shutdown")
async def shutdown_event():
    """
    Close database connection on shutdown
    """
    dal.close_connection()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)