from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from services.dal import DocumentDAL
from services.solider_entity import Document

app = FastAPI(title="Document Management API", version="1.0.0")
dal = DocumentDAL()

class DocumentInputModel(BaseModel):
    """
    Pydantic model for document creation
    """
    id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    rank: Optional[str] = None

@app.post("/documents/", response_model=DocumentInputModel)
async def create_document(document_data: DocumentInputModel):
    """
    Create a new document
    
    Args:
        document_data (DocumentCreate): Document data to create
        
    Returns:
        DocumentResponse: Created document
    """
    try:
        document = Document(
            # id= document_data.id
            first_name=document_data.first_name,
            last_name=document_data.last_name,
            phone_number=document_data.phone_number,
            rank=document_data.rank
        )
        
        success = dal.create(document)
        if success:
            return DocumentInputModel(
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

@app.get("/documents/{doc_id}", response_model=DocumentInputModel)
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
        return document
    else:
        raise HTTPException(status_code=404, detail="Document not found")

@app.get("/items")
def get_items():
    try:
        return dal.get_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/documents/{doc_id}", response_model=dict)
async def update_document(doc_id: str, update_data: DocumentInputModel):
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