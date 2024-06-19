describe('empty spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:31025/')
    cy.get('#hello')
    .should('have.text', 'Great!')
  })
})