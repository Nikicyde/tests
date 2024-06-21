describe('empty spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:30670/')
    cy.get('#hello')
    .should('have.text', 'Great!')
  })
})